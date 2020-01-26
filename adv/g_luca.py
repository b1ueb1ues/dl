if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return G_Luca

class G_Luca(Adv):
    a3 = ('cc',0.13,'hit15')

    conf = {}
    conf['slot.a'] = RR()+LC()
    conf['slot.d'] = Daikokuten()
    conf['acl'] = """
        `s1
        `s2
        `s3, x=5
        """

    def init(this):
        random.seed()
        this.crit_mod = this.custom_crit_mod

        this.s1_crit_mod = Modifier('mod_s1_cc', 'crit', 'chance', 0)
        this.s1_crit_mod.get = this.s1_buff_count
        this.s1_crit_mod.off()
        
        this.a1_crit_mod = Modifier('mod_a1_cc', 'crit', 'chance', 0)
        this.a1_crit_mod.get = this.a1_buff_count
        this.a1_crit_mod.off()

        this.a1_buffs = [
            Selfbuff('a1_sylvan',0.03,20,'crit','chance'),
            Selfbuff('a1_human',0.03,20,'crit','chance'),
            Selfbuff('a1_rokkan',0.03,20,'crit','chance')
        ]
        this.a1_iscding = False

    def prerun(this):
        this.a1_crit_mod.on()

    def buff_icon_count(this):
        # not entirely accurate to game, but works fine in the scope of s2 + the 3 a1 buffs
        return len(set([b.name for b in this.all_buffs]))

    def s1_buff_count(this):
        this.mod_value = 0.10 * this.buff_icon_count()
        return this.mod_value

    def a1_buff_count(this):
        this.mod_value = min(0.04 * this.buff_icon_count(), 0.28)
        return this.mod_value

    def a1_cooldown(this, t):
        this.a1_iscding = False
        log('cd','a1','end')
    
    def custom_crit_mod(this):
        cdmg = this.rand_crit_mod()
        if cdmg > 1 and not this.a1_iscding:
            random.choice(this.a1_buffs).on()
            this.a1_iscding = True
            Timer(this.a1_cooldown).on(3)
        return cdmg

    def s1_proc(this, e):
        with this.s1_crit_mod:
            this.dmg_make('s1',3.14*1)
            this.dmg_make('s1',3.14*1)
            this.dmg_make('s1',3.14*1)
            this.dmg_make('s1',3.14*1)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=1)

