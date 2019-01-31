import adv_test
from adv import *

def module():
    return Linyou

class Linyou(Adv):
    comment = 'new WP & new dragon'
    conf = {
        "mod_a2"  : ('sp' , 'passive'  , 0.08) ,
        "mod_d" :[
            ('att','passive',0.45),
            ('crit','dmg',0.55),
            ],
        "mod_wp" :[
            ('s','passive',0.15),
            ('crit','rate',0.12),
            ],
        }

    def condition(this):
        this.conf['mod_a'] = ('crit' , 'passive', 0.10)
        return 'hp70'
    
    def condition2(this):
        this.conf["mod_wp"] = [
            ('s','passive',0.25),
            ('crit','rate', 0.06),
            ]
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
            this.dmg_make('o_s1_powerup',1.86*2)

    def s2_proc(this, e):
        this.s2ssbuff.on()
        this.s2spdbuff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp
        `s1
        `s2
        `s3
        """
   # # a better acl, but hit threshold of lose one s3.
   # conf['acl'] = """                 
   #     `s2, s1.charged>=s1.sp
   #     `s1
   #     `s3, not this.s2ssbuff.get()
   #     """
    adv_test.test(module(), conf, verbose=0, mass=0)

    module().comment = 'RR+Zephyr'
    module().condition = module().condition2
    conf = {
        "mod_d" :[
            ('att','passive',0.6),
            ],
        "mod_wp" :[
            ('s','passive',0.25),
            ],
        }
    conf['acl'] = """
        `s2, s1.charged>=s1.sp
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

