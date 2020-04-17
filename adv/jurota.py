import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Jurota

class Jurota(Adv):
    a1 = ('bk',0.2)
    conf = {}
    conf['slot.a'] = RR()+ Breakfast_at_Valerios()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5
        `s3
        """
    coab = ['Wand', 'Xander', 'Dagger']

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

