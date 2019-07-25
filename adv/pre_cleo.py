import adv_test
from adv import *
from slot import *
from slot.w import *
from slot.a import *


def module():
    return Veronica

class Veronica(Adv):
    #comment = 'paralysis 3 times'


    def init(this):
        this.s1p = 0 
        this.fsa_charge = 0
        this.fso_dmg = this.conf.fs.dmg
        this.fso_sp = this.conf.fs.sp
        

    def s1_proc(this, e):
        this.s1p += 1
        if this.s1p > 3 :
            this.s1p = 0

        if this.s1p == 1:
            pass
        elif this.s1p == 2:
            this.dmg_make('s1p2_boost',this.conf.s1.dmg/3)
        elif this.s1p == 3:
            this.dmg_make('s1p3_boost',this.conf.s1.dmg/3*2)
        this.conf.fs.dmg = 0
        this.conf.fs.sp = 0
        this.fsa_charge = 1



    def s2_proc(this, e):
        Debuff('s2defdown',0.10,20,0.9).on()



    def fs_proc(this, e):
        if this.fsa_charge:
            this.conf.fs.dmg = this.fso_dmg
            this.conf.fs.sp = this.fso_sp
            this.fsa_charge = 0
            # ground buff doesnt affect by buff time, so use -debuff to emulate that.
            Debuff('a1_str',-0.25,10,1,'att','buff').on()



if __name__ == '__main__':
    conf = {}
    #module().comment = 'RR+SS'
    #conf['slots.a'] = RR()+FoG()
    conf['acl'] = """
        `fs, this.fsa_charge and seq=5
        `s2
        `s1
        """

    adv_test.test(module(), conf, verbose=0)

