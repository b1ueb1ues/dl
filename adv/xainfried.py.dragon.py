import adv.adv_test
import adv.xainfried
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(adv.xainfried.Xainfried):
    conf = adv.xainfried.Xainfried.conf.copy()
    conf['slots.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2
        `fs, x=5
        """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Xainfried, *sys.argv)
