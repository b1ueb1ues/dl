import adv.adv_test
from adv import *
from core.log import *
from slot.a import *
from slot.d import *

def module():
    return V_Orion

class V_Orion(Adv):
    conf = {}

    conf['acl'] = """
        `s3, fsc and not this.s3_buff_on
        `s1, fsc
        `fs, seq=2 and cancel
        """
    conf['slot.a'] = Mega_Friends()+EE()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['afflict_res.burn'] = 0

    def prerun(this):
        this.dc_event = Event('defchain')

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)


    def s2_proc(this, e):
        this.dc_event()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

