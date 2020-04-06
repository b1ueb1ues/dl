import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Rodrigo

class Rodrigo(Adv):
    a1 = ('a',0.08,'hp70')
    conf = {}
    conf['slot.a'] = TSO()+BN()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=3
        """
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+JotS()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

