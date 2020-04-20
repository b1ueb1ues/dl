from core.advbase import *
from slot.a import *

def module():
    return Rodrigo

class Rodrigo(Adv):
    a1 = ('a',0.08,'hp70')
    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=3
        """
    coab = ['Ieyasu','Wand','Cleo']

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+JotS()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)