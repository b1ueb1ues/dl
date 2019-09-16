if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Lea

class Lea(Adv):
    comment = 'c2+fs; no s2'
    a1 = ('fs', 0.50)
    a3 = ('sp', 0.12, 'fs')

    conf = {}
    conf['slot.d'] = Apollo()
    conf['slot.a'] = TSO()+EE()
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100
    
    def s1_proc(this, e):
        this.afflics.burn('s1',120,0.97)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)
