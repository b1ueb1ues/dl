if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    conf = {}
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['cond_afflict_res'] = 0
    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',90,0.6)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

