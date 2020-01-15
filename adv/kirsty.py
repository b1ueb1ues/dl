if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Kirsty

class Kirsty(Adv):
    a3 = ('k_poison',0.3)

    comment = 'no poison'
    conf = {}
    conf['slot.d'] = slot.d.Garland()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        """

    def prerun(this):
        if this.condition('maintain Dauntless Strength'):
            Timer(this.dauntless_strength).on(15)
            Timer(this.dauntless_strength).on(30)
            Timer(this.dauntless_strength).on(45)

    def dauntless_strength(this, t):
        Selfbuff('dauntless_strength',0.20,-1).on()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

