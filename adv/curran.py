import adv_test
import adv
from slot.d import *
from slot.a import *


def module():
    return Curran

class Curran(adv.Adv):
    comment = "no fs"

    a1 = ('od',0.13)
    a3 = ('lo',0.5)

    conf = {}
    conf['slot.a'] = KFM()+CE()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=2
        `s3
        """
    conf['slot.d'] = Shinobi()
    adv_test.test(module(), conf, verbose=-2)
