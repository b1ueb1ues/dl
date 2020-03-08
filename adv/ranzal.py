import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Ranzal

class Ranzal(Adv):
    comment = 'do not use fs'

    conf = {}
    conf['slot.a'] = KFM()+JotS()
    conf['acl'] = """
        `s1 
        `s3
        """

    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = KFM()+CE()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

