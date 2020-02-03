import adv.adv_test
from adv import *
from slot.a.all import *
from slot.d.flame import *

def module():
    return Aurien

class Aurien(Adv):
    comment = 'no s1'
    a1 = ('s',0.4,'hp70')

    conf = {}
    conf['slots.d'] = Apollo()
    conf['acl'] = """
        `s3, x=5 and not this.s3_buff_on
        `s2, x=5
    """
    
    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100

    def s2_proc(this, e):
        this.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)