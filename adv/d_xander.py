import adv.adv_test
from core.advbase import *
from module import energy
from slot.a import *

def module():
    return Dragonyule_Xander

class Dragonyule_Xander(Adv):
    a3 = ('sp',0.05)
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
    adv.adv_test.test(module(), conf)


