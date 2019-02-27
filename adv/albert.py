import adv_test
from adv import *

def module():
    return Albert

class Albert(Adv):
    conf = {
            'mod_a':('fs','passive',0.5),
            's2_recovery':0.9,
            's2_startup':0.25,
            }

    def init(this):
        Timer(this.s2autocharge,1,1).on()
        this.paralyze_count=3
        this.s2buff = Buff("s2_shapshift",1, 20,'ss','ss','self')
        this.a2buff = Buff('a2_str_buff',0.2,20,'att','passive','self')


    def s2autocharge(this, t):
        if not this.a2buff.get():
            this.s2.charge(100)
            log('sp','s2autocharge',100)
            


    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",2.65)

    def fs_proc(this, e):
        if this.paralyze_count > 0:
            if this.s2buff.get():
                this.paralyze_count -= 1
                this.dmg_make("o_s1_paralyze",2.65)

    def s2_proc(this, e):
        this.s2buff.on()
        this.a2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp
        `s1
        `s2
        `fs, seq=2
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

