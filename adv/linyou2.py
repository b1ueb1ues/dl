import adv_test
from adv import *

def module():
    return Linyou

class Linyou(Adv):
    conf = {
            'mod_a2':('sp','passive',0.08)
            }
    conf['mod_d'] = [
            ('crit','damage',0.55),
            ('att','passive',0.45),
            ]
    conf['mod_wp'] = [
            ('crit','rate',0.12),
            ('s','passive',0.15),
            ]

    def condition(this):
        this.conf['mod_a'] = ('crit','rate',0.10)
        return 'hp70'


    def getbleedpunisher(this):
        if this.bleed._static.stacks > 0:
            return 0.08
        return 0

    def init(this):
        this.s2ssbuff = Buff("s2_shapshifts1",1, 10,'ss','ss','self')
        this.s2speedbuff = Buff("s2_speed",0.2, 10,'spd','buff','self')

    def speed(this):
        if this.s2speedbuff.get():
            return 1.2
        else:
            return 1


    def s1_proc(this, e):
        if this.s2ssbuff.get():
            this.dmg_make('o_s1_powerup',1)


    def s2_proc(this, e):
        this.s2ssbuff.on()
        this.s2speedbuff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf,verbose=0)
