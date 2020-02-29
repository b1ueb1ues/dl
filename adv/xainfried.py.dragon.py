import adv.adv_test
import adv.xainfried
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(adv.xainfried.Xainfried):
    conf = adv.xainfried.Xainfried.conf.copy()
    conf['slot.a'] = Resounding_Rendition()+An_Ancient_Oath()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)