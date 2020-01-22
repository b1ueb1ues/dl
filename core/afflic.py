from collections import defaultdict, namedtuple

from core.timeline import *
from core.log import *
import random


class Dot(object):
    """
    Damage over time; e.g. poison
    """

    def __init__(this, name, coef, duration, iv):
        this.name = name
        this.active = 0
        this.coef = coef
        this.iv = iv  # Seconds between each damage tick
        this.duration = duration
        this.true_dmg_event = Event('true_dmg')
        this.true_dmg_event.dname = name
        this.true_dmg_event.dtype = name
        this.true_dmg_event.comment = ''
        this.tick_dmg = 0
        this.quickshot_event = Event('dmg_formula')
        this.tick_timer = Timer(this.tick_proc)
        this.dotend_timer = Timer(this.dot_end_proc)

    def dot_end_proc(this, t):
        log('dot', this.name, 'end\t')
        this.active = 0
        this.tick_timer.off()
        this.cb_end()

    def cb_end(this):
        pass

    def tick_proc(this, t):
        if this.active == 0:
            return
        t.timing += this.iv
        this.true_dmg_event.count = this.tick_dmg
        this.true_dmg_event.on()

    def __call__(this):
        return this.on()

    def get(this):
        return this.active

    def on(this):
        if this.active:
            log('dot', this.name, 'failed\t')
            return 0
        this.active = 1
        this.tick_timer.on(this.iv)
        this.dotend_timer.on(this.duration)
        this.quickshot_event.dmg_coef = this.coef
        this.quickshot_event.dname = this.name
        this.quickshot_event()
        this.tick_dmg = this.quickshot_event.dmg
        log('dot', this.name, 'start\t', '%f/%d' % (this.iv, this.duration))
        return 1

    def off(this):
        this.tick_timer.off()
        this.dotend_timer.off()
        log('dot', this.name, 'end by other reason')


class Afflic(object):
    State = namedtuple("State", "timers resist")

    def __init__(this, name=None):
        this.name = name
        this.resist = 0
        this.rate = 1
        this.tolerance = 0.2
        this.duration = 12
        this.stacking = 1
        this.states = None
        this._get = 0.0

        this.c_uptime = (0, 0)
        this.last_afflict = 0 
        Timer(this.uptime, repeat=1).on(1)

    def get_tolerance(this):
        if this.tolerance > 1:
            return float(this.tolerance) / 100.0
        else:
            return this.tolerance

    def get_rate(this):
        if this.rate > 2:
            return float(this.rate) / 100.0
        else:
            return this.rate

    def get_resist(this):
        if this.resist > 1:
            return float(this.resist) / 100.0
        else:
            return this.resist

    def get(this):
        return this._get

    def update(this):
        total_p = 0.0
        states = defaultdict(lambda: 0.0)
        for state, state_p in this.states.items():
            reduced_state = this.State(frozenset([t for t in state.timers if t.timing > now()]), state.resist)
            states[reduced_state] += state_p
            if reduced_state.timers:
                total_p += state_p
        this.states = states
        this._get = total_p
        return total_p

    def stack_end(this, t):
        this.update()

    def __call__(this, *args, **argv):
        return this.on(*args, **argv)

    def on(this):
        this.resist = this.get_resist()
        this.rate = this.get_rate()
        this.tolerance = this.get_tolerance()
        timer = Timer(this.stack_end, this.duration).on()
        if this.states is None:
            this.states = defaultdict(lambda: 0.0)
            this.states[this.State(frozenset(), this.resist)] = 1.0
        states = defaultdict(lambda: 0.0)
        total_p = 0.0
        for start_state, start_state_p in this.states.items():
            timers = frozenset(list(start_state.timers) + [timer])
            res = start_state.resist
            if res >= 1 or (not this.stacking and any([t.online for t in start_state.timers])):
                states[start_state] += start_state_p
            else:
                rate_after_res = min(1, this.rate - res)
                state_on_succeed = this.State(timers, min(1.0, res + this.tolerance))
                overall_succeed_p = start_state_p * rate_after_res
                overall_fail_p = start_state_p * (1.0 - rate_after_res)
                total_p += overall_succeed_p
                states[state_on_succeed] += overall_succeed_p
                states[start_state] += overall_fail_p
        this.states = states
        this.update()
        return total_p

    def uptime(this, t):
        next_r = this.get()
        next_t = now()
        if next_r == 0:
            this.last_afflict = next_t
        prev_r, prev_t = this.c_uptime
        rate = prev_r + next_r*(next_t-prev_t)
        this.c_uptime = (rate, next_t)
        if next_t > 0 and rate > 0 and next_t % 60 == 0:
            log('{}_uptime'.format(this.name), '{:.2f}/{:.2f}'.format(rate, next_t), '{:.2%}'.format(rate/next_t))

class Afflic_dot(Afflic):
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.coef = 0.97
        this.iv = 3.99
        this.duration = 12

    def on(this, name, rate, coef, duration=None, iv=None):
        this.rate = rate
        this.coef = coef
        if duration:
            this.duration = duration
        if iv:
            this.iv = iv
        dot = Dot('o_%s_%s' % (name, this.name), coef, this.duration, this.iv)
        dot.on()
        r = Afflic.on(this)
        dot.tick_dmg *= r
        return r


class Afflic_cc(Afflic):
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.stacking = 0

    def on(this, name, rate, duration=None):
        this.rate = rate
        if duration:
            this.duration = duration
        return Afflic.on(this)

    def cb_end(this):
        pass


class Afflic_scc(Afflic):
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.stacking = 0

    def on(this, name, rate, duration=None):
        this.rate = rate
        if duration:
            this.duration = duration
        return Afflic.on(this)

    def cb_end(this):
        pass


class Afflics(object):
    def __init__(this):
        this.rinit()
        this.poison = Afflic_dot('poison')
        this.poison.duration = 15
        this.poison.iv = 2.99

        this.burn = Afflic_dot('burn')
        this.burn.duration = 12
        this.burn.iv = 3.99

        this.paralysis = Afflic_dot('paralysis')
        this.paralysis.duration = 13
        this.paralysis.iv = 3.99

        this.blind = Afflic_scc('blind')
        this.blind.duration = 8

        this.bog = Afflic_scc('bog')
        this.blind.duration = 8

        this.freeze = Afflic_cc('freeze')
        this.blind.duration = 4.5

        this.stun = Afflic_cc('stun')
        this.blind.duration = 6.5

        this.sleep = Afflic_cc('sleep')
        this.blind.duration = 6.5

        this.poison.resist = 0
        this.burn.resist = 0
        this.paralysis.resist = 0
        this.blind.resist = 80
        this.bog.resist = 80
        this.freeze.resist = 80
        this.stun.resist = 80
        this.sleep.resist = 80

        this.poison.tolerance = 5
        this.burn.tolerance = 5
        this.paralysis.tolerance = 5
        this.blind.tolerance = 10
        this.bog.tolerance = 20
        this.freeze.tolerance = 20
        this.stun.tolerance = 20
        this.sleep.tolerance = 20

    def add(this, name, atype, rate, duration, coef=0, iv=0):
        if atype == 'burning':
            atype = 'burn'
        if atype == 'para':
            atype = 'paralysis'
        if atype in ['poison', 'burn', 'paralysis']:
            return this.add_dot(name, atype, rate, coef, duration, iv)
        elif atype in ['blind', 'freeze', 'stun', 'sleep', 'bog']:
            return this.add_cc(name, atype, rate, coef, duration, iv)

    def get(this, atype):
        if atype in ['poison', 'burn', 'paralysis']:
            stack = 0
            for i in this.dot:
                if i[0] == atype and i[1].get():
                    stack += 1
            return stack
        elif atype in ['blind', 'freeze', 'stun', 'sleep', 'bog']:
            if atype in this.cc:
                return this.cc[atype].get()

    def r(this):
        return random.random() / this.luck

    def refresh_dot(this):
        tmp = []
        for i in this.dot:
            if i[1].get():
                tmp.append(i)
        this.dot = tmp

    def refresh_cc(this):
        tmp = {}
        for i in this.cc:
            if this.cc[i].get():
                tmp.append(i)
        this.cc = tmp

    def add_dot(this, name, atype, rate, coef, duration, iv):
        if not iv:
            errrrrr()
        if this.resist[atype] < 100:
            r = this.r()
            log('afflic', rate, this.resist[atype], r * 100)
            if rate < this.resist[atype]:
                return 0
            if r * 100 < (rate - this.resist[atype]):
                log('afflic', 'succ', name, atype)
                this.refresh_dot()
                dot = Dot('o_' + name + '_' + atype, coef, duration, iv)
                dot.on()
                this.dot.append((atype, dot))
                this.resist[atype] += 20  # 5
                return 1
        else:
            log('afflic', 'perfect_resist')
        return 0

    def add_cc(this, name, atype, rate, coef, duration, iv):
        if this.resist[atype] < 100:
            r = this.r()
            log('afflic', rate, this.resist[atype], r * 100)
            if atype in this.cc:
                this.cc[atype].on()
                return 0
            elif rate < this.resist[atype]:
                return 0
            elif r * 100 < (rate - this.resist[atype]):
                log('afflic', 'succ', name, atype)
                this.refresh_cc()
                cc = Dot('o_' + name + '_' + atype, 0, duration, duration + 0.01)
                cc.on()
                this.cc[atype] = cc

                if atype == 'blind':
                    this.resist[atype] += 20  # 10
                else:  # elif atype in ['freeze','stun','sleep','bog']:
                    this.resist[atype] += 20
                return 1
        else:
            log('afflic', 'perfect_resist')
        return 0

    def get_uptimes(this):
        uptimes = {}
        for atype in ['poison', 'burn', 'paralysis', 'blind', 'freeze', 'stun', 'sleep', 'bog']:
            aff = this.__dict__[atype]
            rate, t = aff.c_uptime
            # last = aff.last_afflict
            if rate > 0:
                # print('{}_uptime'.format(atype), '{:.2f}/{:.2f}'.format(rate, t), '{:.2%}'.format(rate/t))
                # print('last_{}: {:.2f}s'.format(atype, last))
                uptimes[atype] = rate/t
        return uptimes

    def rinit(this):
        this.resist = {}
        this.resist['poison'] = 0
        this.resist['burn'] = 0
        this.resist['freeze'] = 80
        this.resist['paralysis'] = 80
        this.resist['blind'] = 80
        this.resist['stun'] = 80
        this.resist['curse'] = 0
        this.resist['bog'] = 80
        this.resist['sleep'] = 80
        this.dot = []
        this.cc = {}
        this.luck = 1

