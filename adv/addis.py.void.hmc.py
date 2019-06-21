import adv_test
import addis
from module.bleed import Bleed
from slot.a import *

from slot import *
class blade(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 372 
    a = [('k',0.3), ('prep','50%')]
    conf = {}


def module():
    return Addis

class Addis(addis.Addis):
    pass

if __name__ == '__main__':

    conf = {}
    conf['slot.w'] = blade()
    conf['slots.a'] = Evening_of_Luxury() + RR()
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-260 and seq=5
        `s1, s2.charged<s2.sp
        `fs, this.s2buff.get() and seq=5
        """
    adv_test.test(module(), conf,verbose=0, mass=1)
