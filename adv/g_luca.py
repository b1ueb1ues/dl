from core.advbase import *
from slot.a import *

def module():
    return Gala_Luca

class Gala_Luca(Adv):
    a3 = ('cc',0.13,'hit15')

    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3, x=5
        """
    coab = ['Axe2','Dagger','Peony']

    def init(self):
        self.crit_mod = self.custom_crit_mod
        self.in_s1 = False
        self.a1_buff_types = 3
        self.a1_states = {(None,) * self.a1_buff_types: 1.0}

    def buff_icon_count(self):
        # not entirely accurate to game, but works fine in the scope of s2 + the 3 a1 buffs
        return len(set([b.name for b in self.all_buffs]))

    def custom_crit_mod(self, name):
        if name == 'test':
            return self.solid_crit_mod(name)
        m = {'chance':0, 'dmg':0, 'damage':0, 'passive':0, 'rate':0,}
        for order, modifiers in self.all_modifiers['crit'].items():
            for modifier in modifiers:
                if order in m:
                    m[order] += modifier.get()
                else:
                    raise ValueError(f"Invalid crit mod order {order}")
        base_rate = m['chance']+m['passive']+m['rate']
        crit_dmg = m['dmg'] + m['damage'] + 0.7
        new_states = defaultdict(lambda: 0.0)
        t = now()
        base_icon_count = self.buff_icon_count()
        mean_rate = 0.0

        for start_state, state_p in self.a1_states.items():
            state = tuple([b if b is not None and t - b <= 20.0 else None for b in start_state])  # expire old stacks
            current_rate = base_rate
            icon_count = base_icon_count
            a1_buff_count = len([b for b in state if b is not None])  # active a1buff count
            icon_count += a1_buff_count
            current_rate += 0.03 * a1_buff_count  # a1buff crit
            current_rate += min(0.28, 0.04 * icon_count)  # a1 icon crit
            if self.in_s1:
                current_rate += 0.1 * icon_count  # s1 icon crit
            current_rate = min(1.0, current_rate)
            mean_rate += current_rate * state_p
            
            if state[0] is not None and t - state[0] < 3.0:  # proc in last 3 seconds
                new_states[state] += state_p  # state won't change
            else:
                miss_rate = 1.0 - current_rate
                new_states[state] += miss_rate * state_p

                for i in range(self.a1_buff_types):
                    # t is the newest buff timing so it's in the front; the rest remain in order
                    new_states[(t,) + state[0:i] + state[i + 1:]] += current_rate * state_p / self.a1_buff_types
        self.a1_states = new_states

        return 1.0 + mean_rate * crit_dmg

    def s1_proc(self, e):
        self.in_s1 = True
        self.dmg_make('s1', 3.14)
        self.hits += 1
        self.dmg_make('s1', 3.14)
        self.hits += 1
        self.dmg_make('s1', 3.14)
        self.hits += 1
        self.dmg_make('s1', 3.14)
        self.hits += 1
        self.in_s1 = False

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)