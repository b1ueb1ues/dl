import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Zardin

class Zardin(Adv):
    a1 = ('a',0.10,'hp100')
    
    conf = {}
    conf['slot.a'] = TSO()+Primal_Crisis()
    conf['slot.frostbite.a'] = conf['slot.a']
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    coab = ['Xander', 'Dagger', 'Summer_Estelle']
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+BN()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

