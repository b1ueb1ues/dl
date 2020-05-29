from collections import defaultdict, namedtuple

from core.timeline import *
from core.log import *
import random

AFFLICT_LIST = ['poison', 'paralysis', 'burn', 'blind', 'bog', 'stun', 'freeze', 'sleep', 'frostbite']

class Dot(object):
    """
    Damage over time; e.g. poison
    """

    def __init__(self, name, coef, duration, iv, dtype=None):
        self.name = name
        self.dtype = dtype
        self.active = 0
        self.coef = coef
        self.iv = iv  # Seconds between each damage tick
        self.duration = duration
        self.true_dmg_event = Event('true_dmg')
        self.true_dmg_event.dname = name
        self.true_dmg_event.dtype = dtype if dtype else name
        self.true_dmg_event.comment = ''
        self.tick_dmg = 0
        self.quickshot_event = Event('dmg_formula')
        self.tick_timer = Timer(self.tick_proc)
        self.dotend_timer = Timer(self.dot_end_proc)

    def dot_end_proc(self, t):
        log('dot', self.name, 'end\t')
        self.active = 0
        self.tick_timer.off()
        self.cb_end()

    def cb_end(self):
        pass

    def tick_proc(self, t):
        if self.active == 0:
            return
        t.on(self.iv)
        self.true_dmg_event.count = self.tick_dmg
        self.true_dmg_event.on()

    def __call__(self):
        return self.on()

    def get(self):
        return self.active

    def on(self):
        if self.active:
            log('dot', self.name, 'failed\t')
            return 0
        self.active = 1
        self.tick_timer.on(self.iv)
        self.dotend_timer.on(self.duration)
        self.quickshot_event.dmg_coef = self.coef
        self.quickshot_event.dname = self.name
        self.quickshot_event.dtype = self.dtype if self.dtype else self.name
        self.quickshot_event()
        self.tick_dmg = self.quickshot_event.dmg
        log('dot', self.name, 'start\t', '%f/%d' % (self.iv, self.duration))
        return 1

    def off(self):
        self.tick_timer.off()
        self.dotend_timer.off()
        log('dot', self.name, 'end by other reason')


class AfflicUncapped(object):
    def __init__(self, name=None):
        self.name = name
        self.resist = 0
        self.rate = 1
        self.res_modifier = 0
        self.tolerance = 0.2
        self.duration = 12
        self.states = None
        self.stacks = []
        self._get = 0.0

        self.c_uptime = (0, 0)
        self.last_afflict = 0
        self.event = Event(self.name)

        self.get_override = 0

    def get_tolerance(self):
        if self.tolerance > 1:
            return float(self.tolerance) / 100.0
        else:
            return self.tolerance

    def get_rate(self):
        if self.rate > 2:
            return float(self.rate) / 100.0
        else:
            return self.rate

    def get_resist(self):
        if self.resist > 1:
            return float(self.resist) / 100.0
        else:
            return self.resist

    def get(self):
        return self.get_override or self._get

    def update(self):
        self.uptime()
        nostack_p = 1.0
        for stack_p in self.stacks:
            nostack_p *= 1.0 - stack_p
        self._get = 1.0 - nostack_p

    def stack_end_fun(self, p):
        def end_callback(t):
            self.stacks.remove(p)
            self.update()
        return end_callback

    def __call__(self, *args, **argv):
        return self.on(*args, **argv)

    def set_res_mod(self, delta):
        self.res_modifier = min(self.res_modifier + delta, 1)

    def on(self):
        self.resist = self.get_resist()
        self.rate = self.get_rate()
        self.tolerance = self.get_tolerance()
        if self.states is None:
            self.states = defaultdict(lambda: 0.0)
            self.states[self.resist] = 1.0
        states = defaultdict(lambda: 0.0)
        total_success_p = 0.0
        for res, state_p in self.states.items():
            res -= self.res_modifier
            if res >= self.rate or res >= 1:
                states[res] += state_p
            else:
                rate_after_res = min(1.0, self.rate - res)
                success_p = state_p * rate_after_res
                fail_p = state_p * (1.0 - rate_after_res)
                total_success_p += success_p
                states[res + self.tolerance] += success_p
                states[res] += fail_p
        self.states = states
        self.stacks.append(total_success_p)
        Timer(self.stack_end_fun(total_success_p), self.duration).on()
        self.update()
        
        self.event.rate = total_success_p
        self.event()

        return total_success_p

    def uptime(self):
        next_r = self.get()
        next_t = now()
        if next_r == 0:
            self.last_afflict = next_t
        prev_r, prev_t = self.c_uptime
        rate = prev_r + next_r*(next_t-prev_t)
        self.c_uptime = (rate, next_t)
        if next_t > 0 and rate > 0:
            log('{}_uptime'.format(self.name), '{:.2f}/{:.2f}'.format(rate, next_t), '{:.2%}'.format(rate/next_t))


class AfflicCapped(object):
    State = namedtuple("State", "timers resist")

    def __init__(self, name=None, duration=12):
        self.name = name
        self.resist = 0
        self.rate = 1
        self.res_modifier = 0
        self.tolerance = 0.2
        self.default_duration = duration
        self.duration = duration
        self.stack_cap = 1
        self.states = None
        self._get = 0.0

        self.c_uptime = (0, 0)
        self.last_afflict = 0
        self.event = Event(self.name)

        self.get_override = 0

    def get_tolerance(self):
        if self.tolerance > 1:
            return float(self.tolerance) / 100.0
        else:
            return self.tolerance

    def get_rate(self):
        if self.rate > 2:
            return float(self.rate) / 100.0
        else:
            return self.rate

    def get_resist(self):
        if self.resist > 1:
            return float(self.resist) / 100.0
        else:
            return self.resist

    def get(self):
        return self.get_override or self._get

    def update(self):
        self.uptime()
        total_p = 0.0
        states = defaultdict(lambda: 0.0)
        for state, state_p in self.states.items():
            reduced_state = self.State(frozenset([t for t in state.timers if t.timing > now()]), state.resist)
            states[reduced_state] += state_p
            if reduced_state.timers:
                total_p += state_p
        self.states = states
        self._get = total_p
        return total_p

    def stack_end(self, t):
        self.update()

    def __call__(self, *args, **argv):
        return self.on(*args, **argv)

    def set_res_mod(self, delta):
        self.res_modifier = min(self.res_modifier + delta, 1)

    def on(self):
        self.resist = self.get_resist()
        self.rate = self.get_rate()
        self.tolerance = self.get_tolerance()
        timer = Timer(self.stack_end, self.duration).on()
        if self.states is None:
            self.states = defaultdict(lambda: 0.0)
            self.states[self.State(frozenset(), self.resist)] = 1.0
        states = defaultdict(lambda: 0.0)
        total_p = 0.0
        for start_state, start_state_p in self.states.items():
            res = start_state.resist - self.res_modifier
            if res >= self.rate or res >= 1 or len(start_state.timers) >= self.stack_cap:
                states[start_state] += start_state_p
            else:
                rate_after_res = min(1, self.rate - res)
                succeed_timers = frozenset(list(start_state.timers) + [timer])
                state_on_succeed = self.State(succeed_timers, min(1.0, res + self.tolerance))
                overall_succeed_p = start_state_p * rate_after_res
                overall_fail_p = start_state_p * (1.0 - rate_after_res)
                total_p += overall_succeed_p
                states[state_on_succeed] += overall_succeed_p
                if overall_fail_p > 0:
                    states[start_state] += overall_fail_p
        self.states = states
        self.update()

        self.event.rate = total_p
        self.event()

        return total_p

    def uptime(self):
        next_r = self.get()
        next_t = now()
        if next_r == 0:
            self.last_afflict = next_t
        prev_r, prev_t = self.c_uptime
        rate = prev_r + next_r*(next_t-prev_t)
        self.c_uptime = (rate, next_t)
        if next_t > 0 and rate > 0 and next_t % 60 == 0:
            log('{}_uptime'.format(self.name), '{:.2f}/{:.2f}'.format(rate, next_t), '{:.2%}'.format(rate/next_t))

class Afflic_dot(AfflicUncapped):
    def __init__(self, name=None, duration=12, iv=3.99):
        super().__init__(name)
        self.coef = 0.97
        self.default_duration = duration
        self.duration = duration
        self.default_iv = iv
        self.iv = iv
        self.edge = 0
        self.dot = None

    def on(self, name, rate, coef, duration=None, iv=None, dtype=None):
        self.rate = rate + self.edge
        self.coef = coef
        self.dtype = dtype
        self.duration = duration or self.default_duration
        self.iv = iv or self.default_iv
        self.dot = Dot('o_%s_%s' % (name, self.name), coef, self.duration, self.iv, self.dtype)
        self.dot.on()
        r = super().on()
        self.dot.tick_dmg *= r
        return r

    def timeleft(self):
        if self.dot:
            return self.dot.dotend_timer.timing-now()
        else:
            return 0


class Afflic_cc(AfflicCapped):
    def __init__(self, name=None, duration=6.5):
        super().__init__(name, duration)
        self.stack_cap = 1
        self.edge = 0

    def on(self, name, rate, duration=None):
        self.rate = rate + self.edge
        self.duration = duration or self.default_duration
        return super().on()

    def cb_end(self):
        pass


class Afflic_scc(AfflicCapped):
    def __init__(self, name=None, duration=8):
        super().__init__(name, duration)
        self.stack_cap = 1
        self.edge = 0

    def on(self, name, rate, duration=None):
        self.rate = rate + self.edge
        self.duration = duration or self.default_duration
        return super().on()

    def cb_end(self):
        pass

class Afflic_bog(Afflic_scc):
    def on(self, name, rate, duration=None):
        p = super().on(name, rate, duration)
        if p:
            # from core.advbase import Debuff
            # Debuff('{}_bog'.format(name),-0.5*p,self.duration,1,'att','bog').on()
            from core.advbase import Selfbuff
            buff = Selfbuff('{}_bog'.format(name),0.5*p,self.duration,'att','bog')
            buff.bufftime = buff._no_bufftime
            buff.on()
        return p

class Afflics(object):
    def __init__(self):
        self.rinit()

        self.poison = Afflic_dot('poison', duration=15, iv=2.99)
        self.burn = Afflic_dot('burn', duration=12, iv=3.99)
        self.paralysis = Afflic_dot('paralysis', duration=13, iv=3.99)
        self.frostbite = Afflic_dot('frostbite', duration=21, iv=2.99)

        self.blind = Afflic_scc('blind', duration=8)
        self.bog = Afflic_bog('bog', duration=8)
        self.freeze = Afflic_cc('freeze', duration=4.5)
        self.stun = Afflic_cc('stun', duration=6.5)
        self.sleep = Afflic_cc('sleep', duration=6.5)

        self.poison.resist = 0
        self.burn.resist = 0
        self.paralysis.resist = 0
        self.blind.resist = 80
        self.bog.resist = 100
        self.freeze.resist = 80
        self.stun.resist = 80
        self.sleep.resist = 80
        self.frostbite.resist = 0

        self.poison.tolerance = 5
        self.burn.tolerance = 5
        self.paralysis.tolerance = 5
        self.blind.tolerance = 10
        self.bog.tolerance = 20
        self.freeze.tolerance = 20
        self.stun.tolerance = 20
        self.sleep.tolerance = 20
        self.frostbite.tolerance = 5

    def add(self, name, atype, rate, duration, coef=0, iv=0):
        if atype == 'burning':
            atype = 'burn'
        if atype == 'para':
            atype = 'paralysis'
        if atype in ['poison', 'burn', 'paralysis']:
            return self.add_dot(name, atype, rate, coef, duration, iv)
        elif atype in ['blind', 'freeze', 'stun', 'sleep', 'bog']:
            return self.add_cc(name, atype, rate, coef, duration, iv)

    def get(self, atype):
        if atype in ['poison', 'burn', 'paralysis']:
            stack = 0
            for i in self.dot:
                if i[0] == atype and i[1].get():
                    stack += 1
            return stack
        elif atype in ['blind', 'freeze', 'stun', 'sleep', 'bog']:
            if atype in self.cc:
                return self.cc[atype].get()

    def r(self):
        return random.random() / self.luck

    def refresh_dot(self):
        tmp = []
        for i in self.dot:
            if i[1].get():
                tmp.append(i)
        self.dot = tmp

    def refresh_cc(self):
        tmp = set()
        for i in self.cc:
            if self.cc[i].get():
                tmp.add(i)
        self.cc = tmp

    def add_dot(self, name, atype, rate, coef, duration, iv):
        if not iv:
            raise ValueError('DoT afflict require IV')
        if self.resist[atype] < 100:
            r = self.r()
            log('afflic', rate, self.resist[atype], r * 100)
            if rate < self.resist[atype]:
                return 0
            if r * 100 < (rate - self.resist[atype]):
                log('afflic', 'succ', name, atype)
                self.refresh_dot()
                dot = Dot('o_' + name + '_' + atype, coef, duration, iv)
                dot.on()
                self.dot.append((atype, dot))
                self.resist[atype] += 20  # 5
                return 1
        else:
            log('afflic', 'perfect_resist')
        return 0

    def add_cc(self, name, atype, rate, coef, duration, iv):
        if self.resist[atype] < 100:
            r = self.r()
            log('afflic', rate, self.resist[atype], r * 100)
            if atype in self.cc:
                self.cc[atype].on()
                return 0
            elif rate < self.resist[atype]:
                return 0
            elif r * 100 < (rate - self.resist[atype]):
                log('afflic', 'succ', name, atype)
                self.refresh_cc()
                cc = Dot('o_' + name + '_' + atype, 0, duration, duration + 0.01)
                cc.on()
                self.cc[atype] = cc
                if atype == 'blind':
                    self.resist[atype] += 20  # 10
                else:  # elif atype in ['freeze','stun','sleep','bog']:
                    self.resist[atype] += 20
                return 1
        else:
            log('afflic', 'perfect_resist')
        return 0

    def get_uptimes(self):
        uptimes = {}
        # for atype in ['poison', 'burn', 'paralysis', 'blind', 'freeze', 'stun', 'sleep', 'bog']:
        for atype in AFFLICT_LIST:
            aff = self.__dict__[atype]
            if aff.get_override == 0:
                aff.uptime()
                rate, t = aff.c_uptime
                # last = aff.last_afflict
                if rate > 0:
                    # print('{}_uptime'.format(atype), '{:.2f}/{:.2f}'.format(rate, t), '{:.2%}'.format(rate/t))
                    # print('last_{}: {:.2f}s'.format(atype, last))
                    uptimes[atype] = rate/t
        return uptimes

    def rinit(self):
        self.resist = {}
        self.resist['poison'] = 0
        self.resist['burn'] = 0
        self.resist['freeze'] = 80
        self.resist['paralysis'] = 80
        self.resist['blind'] = 80
        self.resist['stun'] = 80
        self.resist['curse'] = 0
        self.resist['bog'] = 80
        self.resist['sleep'] = 80
        self.dot = []
        self.cc = {}
        self.luck = 1