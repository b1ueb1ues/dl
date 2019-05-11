import adv_test
from adv import *
from module import energy

def module():
    return Pia

class Pia(Adv):

    def pre(this):
        if this.condition('energy'):
            this.init = this.c_init

    def init(this):
        this.conf['acl'] = """
            `s1, seq=5 and cancel 
            `s3, seq=5 and cancel
            """
        energy.Energy(this,{},{})

    def c_init(this):
        energy.Energy(this,{'s2':1},{'s2':1})



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)


