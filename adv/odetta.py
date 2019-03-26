import adv_test
from adv import *

def module():
    return Odetta

class Odetta(Adv):
    
    def pre(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
        if this.condition('hp70'):
            this.conf['mod_a'] = ('att','passive',0.1)
    
    def s1_proc(this, e):
        Buff('s1defdown',-0.02,10,'def','debuff').on()

    def c_s2_proc(this, e):
        Buff('s2',0.15,15*1.2).on()

    def s2_proc(this, e):
        Buff('s2',0.15,15*1.2,wide='self').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=-2)


