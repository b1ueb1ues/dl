import adv_test
import adv
from slot.a import *

def module():
    return Ranzal

class Ranzal(adv.Adv):
    comment = 'do not use fs'

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = KFM()+CE()
        else:
            this.conf.slot.a = KFM()+JotS()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

