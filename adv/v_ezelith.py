if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from module import energy
from slot.a import *

def module():
    return V_Ezelith

class V_Ezelith(Adv):
    a3 = ('bk',0.2)
    conf = {}
    conf['acl'] = """
        `s3,s1.charged>=2803
        `s1
        `s2
        `fs, seq=4
        """
    conf['slot.a'] = RR()+EE()
    conf['cond_afflict_res'] = 0

    def c_prerun(this):
        this.o_prerun()
        this.energy = energy.Energy(this, 
                self={'hit':1},
                team={}
                )

    def prerun(this):
        this.hits = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def init(this):
        if this.condition('never lose combos'):
            this.o_prerun = this.prerun
            this.prerun = this.c_prerun
            this.dmg_proc = this.c_dmg_proc

        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def c_dmg_proc(this, name, amount):
        if name[:2] == 'x1':
            this.hits += 3
        elif name[:2] == 'x2':
            this.hits += 2
        elif name[:2] == 'x3':
            this.hits += 3
        elif name[:2] == 'x4':
            this.hits += 2
        elif name[:2] == 'x5':
            this.hits += 5
        elif name[:2] == 'fs':
            this.hits += 8
        if this.hits >= 35:
            this.energy.add_energy('hit')
            this.hits -= 35

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.hits += 8
            
    def s2_proc(this, e):
        this.hits += 1


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

