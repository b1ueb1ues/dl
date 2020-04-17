import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Karl

class Karl(Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('a',0.15,'hp70')

    conf = {}
    conf['slots.a'] = The_Lurker_in_the_Woods()+Primal_Crisis()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2, cancel
        `fs, seq=2
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

