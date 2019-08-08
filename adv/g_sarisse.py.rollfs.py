import adv.adv_test
import adv
from adv import *
import slot
from slot.a import *
from slot.d import *

def module():
    return G_Sarisse

class G_Sarisse(adv.Adv):
    a3 = ('bt',0.3)
    conf = {}
    #conf['slot.d'] = Cerberus()

    def prerun(this):
        this.hits = 0
        this.bc = adv.Selfbuff()
        this.s2stance = 0


    def init(this):
        if this.condition('never lose combos'):
            this.dmg_proc = this.c_dmg_proc
        this.conf['slot.a'] = FB()+SS()
        if this.condition('rollfs'):
            this.conf['acl'] = """
                `s3,s1.charged>=2803
                `s1,fsc
                `s2,fsc
                `dodge, fsc
                `fs
                """
        else:
#            this.conf['slot.a'] = RR()+FoG()
            this.conf['acl'] = """
                `s3,s1.charged>=2803
                `s1
                `s2
                """
        return 'never lose combos'

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
        if this.hits >= 20:
            this.hits -= 20
            adv.Selfbuff('sylvan strength',0.02,15).on()
            adv.Selfbuff('sylvan crit',0.01,15,'crit','chance').on()

    def s1_proc(this, e):
        buffcount = this.bc.buffcount()
        if buffcount > 7:
            buffcount = 7
        this.dmg_make('s1_missile*%d'%buffcount,0.95*buffcount)
        this.hits += 1 + buffcount
            

    def s2_proc(this, e):
        if this.s2stance == 0:
            adv.Teambuff('s2str',0.20,10).on()
            this.s2stance = 1
        elif this.s2stance == 1:
            adv.Teambuff('s2def',1,15,'defup').on()
            this.s2stance = 0


if __name__ == '__main__':
    conf = {}

    adv_test.test(module(), conf, verbose=-2)

