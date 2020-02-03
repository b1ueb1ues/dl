import adv.adv_test
import adv
from slot.d import *
from slot.a import *

def module():
    return Ranzal

class Ranzal(adv.Adv):
    comment = 'do not use fs'

    conf = {}
    conf['slot.a'] = KFM()+JotS()
    conf['acl'] = """
        `s1 
        `s3
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = KFM()+CE()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

