import adv_test
import adv
from core.log import *
from slot.a import *

def module():
    return V_Orion

class V_Orion(adv.Adv):
    conf = {}

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100
        this.dc_event = Event('defchain')

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)

    def s2_proc(this, e):
        this.dc_event()


if __name__ == '__main__':
    conf = {}

    module().comment = 'no s2'
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3 and cancel
        """
    conf['slots.a'] = The_Shining_Overlord()+LC()
    #conf['slots.a'] = RR()+EE()
    adv_test.test(module(), conf, verbose=0)

