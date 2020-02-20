import adv.adv_test
from core.advbase import *
from module import energy

def module():
    return Elias

class Elias(Adv):
    a3 = ('lo',0.4)
    conf = {}
    conf['acl'] = """
    `s1, fsc
    `s3, fsc
    `fs, seq=4
    """

    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def c_prerun(this):
        energy.Energy(this,{'s2':1},{'s2':1})

    def prerun(this):
        energy.Energy(this,{},{})

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
