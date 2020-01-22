import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return G_Luca

class G_Luca(Adv):
    a3 = ('cc',0.13,'hp70')

    conf = {}
    # conf['slot.a'] = RR()+JotS()
    conf['slot.d'] = Daikokuten()
    # conf['acl'] = """
    #     `s1
    #     `s2, seq=5 and cancel
    #     `s3, seq=5 and cancel
    #     """

    def init(this):
        random.seed()
        this.crit_mod = this.custom_crit_mod

        this.s1_crit_mod = Modifier('mod_crit_s1', 'crit', 'chance', 0)
        this.s1_crit_mod.get = this.s1_buff_count
        this.s1_crit_mod.off()
        
        this.a1_crit_mod = Modifier('mod_crit_a1', 'crit', 'chance', 0)
        this.a1_crit_mod.get = this.a1_buff_count
        # bolb
        this.a1_crit_mod.off()
        this.a1_crit_mod.on()

        this.a1_buffs = [
            Selfbuff('a1_sylvan',0.03,20,'crit','chance'),
            Selfbuff('a1_human',0.03,20,'crit','chance'),
            Selfbuff('a1_rokkan',0.03,20,'crit','chance')
        ]
        this.a1_iscding = False

    def buff_icon_count(this):
        return len(set([b.name for b in this.all_buffs]))

    def s1_buff_count(this):
        this.mod_value = 0.10 * this.buff_icon_count()
        return this.mod_value

    def a1_buff_count(this):
        this.mod_value = min(0.04 * this.buff_icon_count(), 0.28)
        print('a1_buff_count')
        return this.mod_value

    def a1_cooldown(this, t):
        this.a1_iscding = False
        this.buff_icon_count()
        log('cd','a1','end')
    
    def custom_crit_mod(this):
        cdmg = this.rand_crit_mod()
        if cdmg > 1 and not this.a1_iscding:
            a1_buff = random.choice(this.a1_buffs)
            a1_buff.on()
            this.a1_iscding = True
            Timer(this.a1_cooldown).on(3)
        return cdmg

    def s1_proc(this, e):
        this.s1_crit_mod.on()
        s1_hit1 = 6.50
        s1_hit2 = 1.50
        this.dmg_make('s1',s1_hit1*1)
        this.dmg_make('s1',s1_hit2*1)
        this.dmg_make('s1',s1_hit2*1)
        this.dmg_make('s1',s1_hit2*1)
        this.s1_crit_mod.off()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=0)

