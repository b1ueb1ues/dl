import adv_test
from adv import *

def module():
    return Lathna

class Lathna(Adv):
    comment = 'no poison'
    a1 = ('k_poison',0.15)
    
    conf = {}
    conf['slot.d'] = slot.d.Shinobi()
    conf['acl'] = """
        # s1a = this.s1a
        `s1a
        `s2, seq = 5
        `s3, seq = 5
        """

    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            with Modifier("s1killer", "poison_killer", "hit", 0.5):
                this.dmg_make("s1", 2.37*4)
            this.conf.s1.recovery = 4.05
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0 
    
    def s1_proc(this, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s1", 2.37*3)

    def s2_proc(this, e):
        with Modifier("s2killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s2", 17.26)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

