import adv_test
from adv import *

def module():
    return Odetta

class Odetta(Adv):
    
    def condition(this):
        this.s2_proc = this.c_s2_proc
        this.conf['mod_a'] = ('att','passive',0.1)
        return 'hp70 & buff all team'
    
    def s1_proc(this, e):
        Buff('s1defdown',-0.02,10,'def','debuff').on()

    def c_s2_proc(this, e):
        Buff('s2',0.15,15).on()

    def s2_proc(this, e):
        Buff('s2',0.15,15,wide='self').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=3
        """
    adv_test.test(module(), conf, mass=0)


