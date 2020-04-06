import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Malka

class Malka(Adv):
    comment = ''

    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['slot.a'] = RR()+BN()

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = RR()+JotS()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

