import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d.flame import *
def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')
    conf = {}
    conf['slot.a'] = Twinfold_Bonds()+The_Lurker_in_the_Woods()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=2
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

