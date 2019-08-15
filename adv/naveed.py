if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
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
        if adv_test.sim_duration == 60:
            this.conf['slots.a'] = First_Rate_Hospitality()+The_Shining_Overlord()
        elif sim_duration == 90:
            this.conf['slots.a'] = First_Rate_Hospitality()+The_Shining_Overlord()
        elif sim_duration == 180:
            this.conf['slot.a'] = The_Shining_Overlord()+Jewels_of_the_Sun()
            this.conf['s2stop'] = 1


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

