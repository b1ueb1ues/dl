if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Joe

class Joe(adv.Adv):
    conf = {}
    #conf['slots.a'] = RR()+EE()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, fsc
        `fs, seq=4
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

        if this.condition('hp100'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',100+70*this.fullhp,0.803)
        
    def s2_proc(this, e):
        this.afflics.burn('s2',100+70*this.fullhp,0.803)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

