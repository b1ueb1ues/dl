if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.bleed import Bleed
import addis
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
    comment = 'v534 against HMC; '
    conf = {}
    conf['slot.w'] = blade()
    conf['slots.a'] = SSP() + RR()

    conf['acl'] = """
        # bs = this.bleed._static['stacks']
        `s2, s1.charged>=s1.sp-260 and seq=5 and bs != 3
        `s1, s2.charged<s2.sp and bs != 3
        `s3, not this.s2buff.get()
        `fs, this.s2buff.get() and seq=5
        """



if __name__ == '__main__':
    adv_test.test(module(), conf,verbose=0, mass=1)

