import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Laxi

class Laxi(Adv):
    comment = "a1 proc at 0s"
    
    conf = {}
    conf['slot.a'] = HoH()+DD()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2, not this.s2buff.get()
        `s1
        """

    def prerun(this):
        this.hp = 0.0
        
        this.healed = 0
        this.heal = Action('heal')
        this.heal.conf.startup = 0.1
        this.heal.conf.recovery = 5.0

        this.heal_initial = Timer(this.heal_proc,0).on()
        this.s2buff = Selfbuff("s2",0.15,-1,toggle=True)
        this.s2tick = Timer(this.s2_tick,2.9,1)

        this.a3buff = Selfbuff("a3",0.2,-1,"att","passive")

    def s1_proc(this, e):
        if this.s2buff.get() != 0:
            this.dmg_make("o_s1_boost",0.87*4)

    def s2_proc(this, e):
        this.s2buff.on()
        # if not this.s2buff.get():
        #     this.s2buff.on()
        #     this.s2tick.on()
        # else:
        #     this.s2buff.off()
        #     this.s2tick.off()

    def s2_tick(this, t):
        if this.hp >= 4.0:
            this.hp -= 3.5
        if this.hp <= 30.0:
            this.a3buff.on()
            if this.healed == 0:
                this.heal_proc(None)
        else:
            this.a3buff.off()

    def heal_proc(this, t):
        this.healed = 1
        this.hp = 100.0
        this.s2buff.off()
        this.s2tick.off()
        #this.a3buff.off()

        this.heal.getdoing().cancel_by.append('heal')
        this.heal.getdoing().interrupt_by.append('heal')
        this.heal()
if __name__ == '__main__':
    adv.adv_test.test(module(), conf, verbose=0)

