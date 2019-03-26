import adv_test
import adv
from adv import *
from module import energy

def module():
    return V_Ezelith

class V_Ezelith(Adv):
    conf = {
            "mod_a2":('att','broken_p',0.2*0.15),
            }

    def c_init(this):
        this.o_init()
        this.energy = energy.Energy(this, 
                self={'hit':1},
                team={}
                )

    def init(this):
        this.hits = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )
        this.dmg_make("o_s1_burn",0.883*3)
        this.dmg_make("o_s1_burn",0.883*3)
        this.dmg_make("o_s1_burn",0.883*3)

    def pre(this):
        if this.condition('never lose combos'):
            this.o_init = this.init
            this.init = this.c_init
            this.dmg_proc = this.c_dmg_proc
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s3,s1.charged>=2803
                `s1
                `s2
                `fs, seq=4
                """

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
        this.hits += 8
            
    def s2_proc(this, e):
        this.hits += 1
        Buff('defdown',-0.09,10,'def').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s3,s1.charged>=s1.sp
        `s1
        `s2
        """
    adv_test.test(module(), conf, verbose=0)

