import adv.adv_test
from core.advbase import *
import slot.a 
from slot.a import *
from slot.d import *

def module():
    return Cibella

class Cibella(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    coab = ['Blade', 'Xander', 'Dagger']
    conf['slots.a'] = RR() + Breakfast_at_Valerios()
    conf['slots.d'] = Leviathan()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
