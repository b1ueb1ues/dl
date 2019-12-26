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
        `s1, fsc
        `s2, fsc
        `s3, fsc
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
        this.afflics.burn('s2',90+70*this.fullhp,0.6)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

