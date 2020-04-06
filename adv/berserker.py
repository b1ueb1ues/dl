from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `fs, x=3
        """

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+JotS()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)