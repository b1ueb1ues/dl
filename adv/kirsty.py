import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Kirsty

class Kirsty(adv.Adv):
    a3 = ('k_poison',0.3)

    comment = 'no poison'

    def prerun(this):
        if this.condition('maintain Dauntless Strength'):
            adv.Timer(this.dauntless_strength).on(15)
            adv.Timer(this.dauntless_strength).on(30)
            adv.Timer(this.dauntless_strength).on(45)

    def dauntless_strength(this, e):
        adv.Buff('dauntless_rampart',0.15,-1,'att','passive').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        """
    conf['slot.d'] = Vayu()
    adv_test.test(module(), conf, verbose=0)

