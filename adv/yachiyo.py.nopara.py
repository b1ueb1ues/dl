if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *
import yachiyo

def module():
    return Yachiyo

class Yachiyo(yachiyo.Yachiyo):
    #comment = 'paralysis 3 times'

    def prerun(this):
        super(Yachiyo, this).prerun()
        this.afflics.paralysis.resist=100


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
    module().comment = 'RR+SS'
    from slot.a import *
    conf['slots.a'] = RR()+Stellar_Show()
    conf['acl'] = """
        `fs, this.fsa_charge and seq=5
        `s2
        `s1
        """
    adv_test.test(module(), conf, verbose=0)

