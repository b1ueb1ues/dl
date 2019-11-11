if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Karina

class Karina(adv.Adv):
    a3 = ('prep','50%')
    conf = Conf()
    conf.slot.a = KFM()+CE()
    conf['acl'] = """
        `s1
        `s2, seq=4
        `s3, fsc
        `fs, seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)