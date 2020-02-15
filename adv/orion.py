import adv.adv_test
from core.advbase import *

def module():
    return Orion

class Orion(Adv):
    a1 = ('cc',0.10,'hit15')
    conf = {}
    conf['acl'] = """
    `s1, x=5
    `s2, seq=4 and cancel or fsc
    `s3, seq=4 and cancel or fsc
    `fs, seq=4 and s1.charged <= s1.sp - 288
    """

    def prerun(this):
        this.charge_p('prep','50%')


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

