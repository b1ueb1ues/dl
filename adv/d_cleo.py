import adv_test
import adv
from adv import *
from module import energy

def module():
    return D_Cleo

class D_Cleo(adv.Adv):
    def pre(this):
        if this.condition('hp70'):
            this.conf['mod_a'] = ('att' , 'passive', 0.13) 
        if this.condition('energy'):
            this.init = this.c_init
        if this.condition('always connect hits'):
            this.dmg_proc = this.c_dmg_proc

    def c_init(this):
        this.stance = 0
        this.hits = 0
        this.energy = energy.Energy(this, 
                self={'s1':1,'hit':1},
                team={'s1':1}
                )
    def init(this):
        this.stance = 0
        this.hits = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def c_dmg_proc(this, name, amount):
        if name == 'x1':
            this.hits += 1
        elif name == 'x2':
            this.hits += 2
        elif name == 'x3':
            this.hits += 2
        elif name == 'x4':
            this.hits += 1
        elif name == 'x5':
            this.hits += 1
        elif name == 'fs':
            this.hits += 3
        elif name == 's1':
            this.hits += 11
        elif name == 's2':
            this.hits += 5
        if this.hits >= 30:
            this.energy.add_energy('hit')
            this.hits -= 30

    def s1_proc(this, e): # buggy lvl3 s1
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
            adv.Buff('s1s',0.1,10,'att').on()
        elif this.stance == 2:
            this.stance = 0
            adv.Buff('s1s',0.1,10,'att').on()
            adv.Buff('s1c',0.08,10,'crit','chance').on()




if __name__ == '__main__':
    module().comment = 's1 in lvl3 (buggy)'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0)

    conf['s1_sp'] = 2400
    conf['s1_dmg'] = 0.63*11
    conf['str_adv'] = 474-17
    module().comment = 'use s1 in lvl2'
    adv_test.test(module(), conf, verbose=0)
