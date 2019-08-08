import adv.adv_test
import adv
from slot.a import *

def module():
    return Karina

class Karina(adv.Adv):
    a3 = ('prep','50%')
    conf = Conf()
    conf.slot.a = KFM()+CE()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)

