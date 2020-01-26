if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Veronica

class Veronica(adv.Adv):
    a3 = ('prep','100%')
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5 and s1.charged >= 2500
        """

    def prerun(this):
        adv.Teambuff('last',2.28,1).on()
        this.hp = 80

    def s1_proc(this, e):
        with adv.CrisisModifier('s1', 2.25, this.hp):
            this.dmg_make('o_s1_crisis', this.conf.s1.dmg)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

