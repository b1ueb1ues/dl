import adv.adv_test
import adv
from slot.a import *

def module():
    return Naveed

class Naveed(adv.Adv):
    def prerun(this):
        this.s1level = 0
        this.charge_p('prep','100%')
        pass

    def s1_proc(this, e):
        this.dmg_make("o_s1_missile",3*this.s1level*0.28)

    def debug(this):
        this.s1level = 5


    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level >= 5:
            if this.conf.s2stop :
                this.s2.sp = 0
            this.s1level = 5
        adv.Event('defchain')()

        
        


if __name__ == '__main__':
    conf = {}

    import sys
    from slot.a import *
    if len(sys.argv) >= 3:
        sim_duration = int(sys.argv[2])
    else:
        sim_duration = 180

    if sim_duration == 60:
        conf['slots.a'] = First_Rate_Hospitality()+The_Shining_Overlord()
    elif sim_duration == 90:
        conf['slots.a'] = First_Rate_Hospitality()+The_Shining_Overlord()
    elif sim_duration == 180:
        conf['slot.a'] = The_Shining_Overlord()+Jewels_of_the_Sun()
        conf['s2stop'] = 1

    conf['acl'] = """
        `s2, sp 
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

