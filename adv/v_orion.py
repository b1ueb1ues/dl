if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from core.log import *
from slot.a import *

def module():
    return V_Orion

class V_Orion(adv.Adv):
    conf = {}

    comment = 'no s2'
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3 and cancel
        """
    conf['slots.a'] = TSO()+EE()
    conf['cond_afflict_res'] = 0

    def prerun(this):
        this.afflics.burn.maxdepth = 15
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100
        this.dc_event = Event('defchain')

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)


    def s2_proc(this, e):
        this.dc_event()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

