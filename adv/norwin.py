import adv.adv_test
from adv import *

def module():
    return Norwin

class Norwin(Adv):
    a3 = ('k_blind', 0.20)
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['cond_afflict_res'] = 80

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.blind.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.blind.resist=100

    def s1_proc(this, e):
        this.afflics.blind('s1',100)
        Teambuff('a1',0.15*this.afflics.blind.get(),10).on()


    def s2_proc(this, e):
        with Modifier("s1killer", "blind_killer", "hit", 0.44):
            this.dmg_make('s1',3*2.45)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
