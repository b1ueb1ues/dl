import adv_test
import adv
from module import energy
from slot.a import *

def module():
    return D_Xander

class D_Xander(adv.Adv):
    a3 = ('sp',0.05)


    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun


    def prerun(this):
        energy.Energy(this,
                self={},
                team={}
                )

    def c_prerun(this):
        energy.Energy(this,
                self={'s2':1},
                team={'s2':1}
                )


if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel or s
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    conf['acl'] = acl12
    adv_test.test(module(), conf, verbose=0)


