import adv.adv_test
from adv import *
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
    

    def d_slots(this):
        this.slots.a = RR()+CE()  # c5 s2 fs s1  break comboes
        this.slots.a = RR()+JotS()  # wand c2*1.08 = 217
        this.slots.d = Shinobi()

    def d_acl(this):
        if 'blade' in this.ex:
            pass
        if this.condition('always in a1'):
            this.conf['acl'] = """
                `rotation
                """
            this.conf['rotation_init'] = """
                s2s1
                c5c4s1
            """
            this.conf['rotation'] = """
                c5s2c5s1
                c5c4s1
            """

    def prerun(this):
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


        

    def s1_proc(this, e):
        this.s1p += 1
        if this.s1p > 3 :
            this.s1p = 1

        if this.s1p == 1:
            this.dmg_make('s1',3.53*3)
        elif this.s1p == 2:
            this.dmg_make('s1',3.53*3)
            this.dmg_make('s1p2_boost',3.53)
        elif this.s1p == 3:
            this.dmg_make('s1',3.53*3)
            this.dmg_make('s1p2_boost',3.53*2)

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
            Debuff('a1_str',-0.25,10,1,'att','buff').on()



if __name__ == '__main__':
    conf = {}
    #module().comment = 'RR+SS'
    #conf['slots.a'] = RR()+FoG()

    conf['acl'] = """
        `s2
        `s1
        """

    adv_test.test(module(), conf, verbose=0)

