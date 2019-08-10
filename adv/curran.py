if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Curran

class Curran(adv.Adv):
    comment = "no fs"
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=2
        `s3
        """
    a1 = ('od',0.13)
    a3 = ('lo',0.5)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
