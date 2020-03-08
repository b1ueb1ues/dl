import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Erik

class Erik(Adv):
    comment =''
    a1 = ('fs',0.30)
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs,seq=5
        """
    conf['slot.a'] = KFM()+CE()
    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = KFM()+JotS()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

