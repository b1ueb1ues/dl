if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Luca

class Luca(adv.Adv):
    a1 = ('a',0.13,'hp100')
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['cond_afflict_res'] = 0

    conf = {}
    conf['slot.a'] = SotS()+Dear_Diary()
    conf['slot.d'] = C_Phoenix()

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

    def s1_proc(this, e):
        this.afflics.paralysis('s1',110,0.883)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)
