if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')
    conf = {}
    conf['cond_afflict_res'] = 0
    conf['slot.a'] = TB()+EE()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, cancel
        `s2, cancel
        `fs, x=5
        """

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

