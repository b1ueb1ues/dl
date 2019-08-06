import adv_test
import adv
from slot.a import *
import slot.a
from slot.d import *

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c5'

    a3 = ('fs',0.50)

    conf = {}

    def s1_proc(this, e):
        this.dmg_make('o_s1_boost',this.conf.s1.dmg*0.05*5)



if __name__ == '__main__':
    conf = {}
    conf['slots.a'] = TSO()+JotS()
    conf['slots.d'] = DJ()
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, x=2
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

