import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Delphi

class Delphi(Adv):
    comment = 'Fatalis > Chthonius(1+ shift) > Marishiten > Shinobi'
    a1 = ('a',-0.55)

    conf = {}
    conf['slot.a'] = Mega_Friends()+The_Plaguebringer()
    conf['acl'] = """
        `s1
        `s2, this.s1fscharge == 0 and (s1.charged <= ((s1.sp/13)*9))
        `s3
        `fs, x=2 and (this.s1fscharge == 0 or this.hits >= 15)
    """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.poison.resist=100

        this.flurry_poison = 70
        
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0

        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

        this.skilltimer = Timer(this.skillautocharge,1,1).on()
        this.s1fscharge = 0

    def skillautocharge(this, t):
        this.s1.charge(999999.0*0.08)
        this.s2.charge(999999.0*0.05)
        log('sp','s1autocharge')

    def s1_proc(this, e):
        Debuff('s1defdown',0.20,10,1).on()
        this.s1fscharge = 1
        this.dmg_make('o_s2_reflect', this.s2reflect * 11, fixed=True)
    
    def s2_proc(this, e):
        this.afflics.poison('s2',120+this.flurry_poison*(this.hits>=15),3.00,27)

    def fs_proc(this, e):
        if this.s1fscharge > 0:
            this.s1fscharge -= 1
            this.dmg_make("o_fs_boost",0.21*3)
            this.afflics.poison('fs',120+this.flurry_poison*(this.hits>=15),3.00,27)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=0)
