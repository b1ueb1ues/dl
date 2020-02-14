import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Vanessa

class Vanessa(Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = KFM()+Mega_Friends()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, cancel
        `s2, fsc
        `fs, x=4
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

