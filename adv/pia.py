import adv.adv_test
from core.advbase import *
from module import energy

def module():
    return Pia

class Pia(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, seq=5
        `fs, seq=5
        """

    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        energy.Energy(this,{},{})

    def c_prerun(this):
        energy.Energy(this,{'s2':1},{'s2':1})



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


