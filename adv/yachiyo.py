import adv_test
import adv

def module():
    return Yachiyo

class Yachiyo(adv.Adv):
    #comment = 'paralysis 3 times'

    def init(this):
        this.para_last = 0
        if this.condition('paralysis*3'):
            this.para_last = 3
        
        this.fsa_charge = 0
        

    def s1_before(this, e):
        if this.para_last > 0:
            this.para_last -= 1
            this.dmg_make("o_s1_paralysis",1.98)
            adv.Buff('a1',0.15,10).on()
            adv.Buff('para killer',0.20,13,'att','killer').on()
            return 8.64*0.86231884 # para only affect the second hit 

    def s2_proc(this, e):
        this.fso_dmg = this.conf.fs.dmg
        this.fso_sp = this.conf.fs.sp
        this.conf.fs.dmg = 7.82
        this.conf.fs.sp = 200
        this.fsa_charge = 1

    def fs_proc(this, e):
        if this.fsa_charge:
            this.conf.fs.dmg = this.fso_dmg
            this.conf.fs.sp = this.fso_sp
            this.fsa_charge = 0



if __name__ == '__main__':
    conf = {}
    #module().comment = 'RR+SS'
    from slot.a import *
    conf['slots.a'] = RR()+Stellar_Show()
    conf['acl'] = """
        `fs, this.fsa_charge and seq=5
        `s2
        `s1
        """
    adv_test.test(module(), conf, verbose=0)

