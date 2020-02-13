import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *
from slot.w import *

class w530(WeaponBase):
    ele = ['water','light']
    wt = 'blade'
    att = 468


def module():
    return Yachiyo

class Yachiyo(Adv):
    a3 = ('k_paralysis', 0.2)
    conf = {}
    conf['slots.a'] = MF()+SotS()
    conf['slots.d'] = Corsaint_Phoenix()
    conf['acl'] = """
        `fs, this.fsa_charge and seq=5
        `s2
        `s1
        `s3
        """
    conf['afflict_res.paralysis'] = 0

    def prerun(this):
        this.fsa_charge = 0        

    def s1_proc(this, e):
        this.dmg_make('s1',4.32)
        this.afflics.paralysis('s1',100,0.66)
        Selfbuff('a1',0.15*this.afflics.paralysis.get(),10).on()
        this.dmg_make('s1',4.32)


    def s2_proc(this, e):
        # this.fso_dmg = this.conf.fs.dmg
        this.fso_sp = this.conf.fs.sp
        # this.conf.fs.dmg = 7.82
        this.conf.fs.sp = 200
        this.fsa_charge = 1

    def fs_proc(this, e):
        if this.fsa_charge:
            # this.conf.fs.dmg = this.fso_dmg
            this.dmg_make("o_fs_boost",6.90)
            this.conf.fs.sp = this.fso_sp
            this.fsa_charge = 0



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

