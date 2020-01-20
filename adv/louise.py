if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from core.advbase import Modifier
from slot.a import *
from slot.d import *

def module():
    return Louise

class Louise(adv.Adv):
    a1 = ('od',0.13)
    comment = 'no fs'
    conf = {}
    conf['slot.a'] = DD()+TP()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.poison.resist=100


    def s1_proc(this, e):
        this.afflics.poison('s1', 120, 0.582)


    def s2_proc(this, e):
        with Modifier("s2killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s2", 8.07)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)
