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
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = TSO()+JotS()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

