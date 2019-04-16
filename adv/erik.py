import adv_test
import adv
from slot.a import *

def module():
    return Erik

class Erik(adv.Adv):
    comment ='do not use weapon skill'

    a1 = ('fs',0.30)
    comment += '& reach 100 resist with Silke Lends a Hand'

    conf = {'slots.a': RR()+Silke_Lends_a_Hand()}
    def debug(this):
        print this.all_modifiers



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,fsc
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

