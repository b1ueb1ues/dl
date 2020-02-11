import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return G_Luca

class G_Luca(Adv):
    a3 = ('cc',0.13,'hit15')

    conf = {}
    conf['slot.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slot.d'] = Daikokuten()
    conf['acl'] = """
        `dragon, s=2
        `s1
        `s2
        `s3, x=5
        """

    def init(this):
        this.crit_mod = this.custom_crit_mod
        this.in_s1 = False
        this.a1_buff_types = 3
        this.a1_states = {(None,) * this.a1_buff_types: 1.0}

    def buff_icon_count(this):
        # not entirely accurate to game, but works fine in the scope of s2 + the 3 a1 buffs
        return len(set([b.name for b in this.all_buffs]))

    def custom_crit_mod(this):
        base_rate = 0.0
        crit_dmg = 0.7
        for i in this.all_modifiers:
            if 'crit' == i.mod_type:
                if i.mod_order in ['passive', 'rate', 'chance']:
                    base_rate += i.get()
                if i.mod_order in ['dmg', 'damage']:
                    crit_dmg += i.get()
        new_states = defaultdict(lambda: 0.0)
        t = now()
        base_icon_count = this.buff_icon_count()
        mean_rate = 0.0

        for start_state, state_p in this.a1_states.items():
            state = tuple([b if b is not None and t - b <= 20.0 else None for b in start_state])  # expire old stacks
            current_rate = base_rate
            icon_count = base_icon_count
            a1_buff_count = len([b for b in state if b is not None])  # active a1buff count
            icon_count += a1_buff_count
            current_rate += 0.03 * a1_buff_count  # a1buff crit
            current_rate += min(0.28, 0.04 * icon_count)  # a1 icon crit
            if this.in_s1:
                current_rate += 0.1 * icon_count  # s1 icon crit
            current_rate = min(1.0, current_rate)
            mean_rate += current_rate * state_p
            
            if state[0] is not None and t - state[0] < 3.0:  # proc in last 3 seconds
                new_states[state] += state_p  # state won't change
            else:
                miss_rate = 1.0 - current_rate
                new_states[state] += miss_rate * state_p

                for i in range(this.a1_buff_types):
                    # t is the newest buff timing so it's in the front; the rest remain in order
                    new_states[(t,) + state[0:i] + state[i + 1:]] += current_rate * state_p / this.a1_buff_types
        this.a1_states = new_states

        return 1.0 + mean_rate * crit_dmg

    def s1_proc(this, e):
        this.in_s1 = True
        this.dmg_make('s1', 3.14)
        this.hits += 1
        this.dmg_make('s1', 3.14)
        this.hits += 1
        this.dmg_make('s1', 3.14)
        this.hits += 1
        this.dmg_make('s1', 3.14)
        this.hits += 1
        this.in_s1 = False

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
