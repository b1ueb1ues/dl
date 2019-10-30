if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
import adv
from slot.a import *

def module():
    return Naveed

class Naveed(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s2, sp 
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+BN()
        else:
            this.conf.slot.a = TSO()+JotS()
            
    def prerun(this):
        this.s1level = 0
        this.charge_p('prep','100%')
        pass

    def s1_proc(this, e):
        this.dmg_make("s1_missile",3*this.s1level*0.28)


    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level >= 5:
            if this.conf.s2stop :
                this.s2.sp = 0
            this.s1level = 5
        adv.Event('defchain')()

        
        


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

