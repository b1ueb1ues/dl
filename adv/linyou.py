import adv_test
from adv import *

def module():
    return Linyou

class Linyou(Adv):

    def condition(this):
        this.conf['mod_a'] = ('crit' , 'passive', 0.10)
        return 'hp70'
    
    def init(this):
        this.s2ssbuff = Buff("s2_s1",1, 10, 'ss','ss', wide='self')
        this.s2spdbuff = Buff("s2_spd",0.2, 10, 'spd', wide='self')

    def speed(this):
        if this.s2spdbuff.get():
            return 1.2
        return 1
    

    def s1_proc(this, e):
        if this.s2ssbuff.get():
            this.dmg_make('o_s1_powerup',1.86*3)

    def s2_proc(this, e):
        this.s2ssbuff.on()
        this.s2spdbuff.on()


if __name__ == '__main__':
    conf = {
        }
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

