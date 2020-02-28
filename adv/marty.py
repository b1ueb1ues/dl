import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Marty

class Marty(Adv):
    a1 = ('sp',0.05)
    conf = {}
    conf['slots.a'] = Mega_Friends()+BN()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, fsc and not this.s3_buff
        `s1, fsc
        `fs, seq=2
        """



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

