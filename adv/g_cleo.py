import adv.adv_test
from core.advbase import *
from slot import *
from slot.w import *
from slot.a import *
from slot.d import *
from module.fsalt import *

import random
random.seed()


def module():
    return G_Cleo

class G_Cleo(Adv):
    comment = '(the true cleo is here)'
    a3 = ('prep','100%')
    conf = {}
    conf['slot.a'] = CC()+JotS()  # wand c2*1.08 = 217
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s2, pin='prep'
        `fs, s1.charged>=s1.sp and this.fsa_charge
        `s2, x=5 or x=4 or fsc
        `s1, s=2 or fsc
        `s3, x=5 or fsc
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.slots.a = CC()+Primal_Crisis()

    def prerun(this):
        this.a1_buffed = this.condition('always in a1')
        this.s1p = 0 
        this.fsa_charge = 0
        #this.fso_dmg = this.conf.fs.dmg
        #this.fso_sp = this.conf.fs.sp

        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf({
                'fs.dmg':0,
                'fs.sp' :0,

                "fs.startup":43/60.0,
                "x5fs.startup":57/60.0,

                "fs.recovery":67/60.0,
                })
        this.fs_alt = Fs_alt(this, this.fsaconf)




    def s1_dmg(this, t):
        this.dmg_make('s1_hit_single',0.88)
        this.hits += 1
        this.dmg_make('s1_hit_aoe',2.65)
        this.hits += 1

    def s1_proc(this, e):
        this.s1p += 1
        if this.s1p > 3 :
            this.s1p = 1
        if this.s1p == 1:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
        elif this.s1p == 2:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*3 )/60)
        elif this.s1p == 3:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*3 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*4 )/60)

        this.fs_alt.on()
        #this.conf.fs.dmg = 0
        #this.conf.fs.sp = 0
        this.fsa_charge = 1


    def fs_proc(this, e):
        if this.fsa_charge:
            #this.conf.fs.dmg = this.fso_dmg
            #this.conf.fs.sp = this.fso_sp
            this.fsa_charge = 0
            this.fs_alt.off()
            # ground buff doesnt affect by buff time, so use -debuff to emulate that.
            if this.a1_buffed:
                Debuff('a1_str',-0.25,10,1,'att','buff').on()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
