import adv_test
from adv import *
from slot.a import *
from slot.d import *
import random
from slot import *

class E(Amulet):
    att = 54
    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('Elegant_Escort','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        log('debug','getbane', this.adv.afflic.get()*0.3 )
        return this.adv.afflic.get()*0.3


def module():
    return Rena

class Rena(Adv):
    def prerun(this):
        if this.condition('0 burn resist'):
            this.afflic = Afflic()
            this.afflic.resist = 0
            this.afflic.rate = 1.2
            this.afflic.tolerance = 0.2
        else:
            this.afflic = Afflic()
            this.afflic.resist = 0.55
            this.afflic.rate = 1.2
            this.afflic.tolerance = 0.2
        this.a1_iscding = 0
        this.stance = 0
        random.seed()

    
    def s1_proc(this, e):
        coef_x_chance = this.afflic.on() * 0.97
        Dot('o_s1_burn',coef_x_chance, 12, 3.9).on()
        #this.afflics.add('s1','burn',120, 12, 0.97, 3.9)

        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
        elif this.stance == 2:
            this.stance = 0
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
            coef = this.conf.s1.dmg*0.8* this.afflic.get()
            if coef:
                log('debug','s1_boost', this.afflic.get())
                this.dmg_make("o_s1_boost", coef)



    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')

    def a1_act(this):
        #logcat()
        #print this.a1_iscding
        #exit()
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.0,10,'def').on()
            #Teambuff('db_test',0.10,15).on()
            Event('defchain')()
        else:
            log('cd','a1','trigger failed')

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()
        return r


if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = RR()+E()
    #conf['slot.a'] = RR()+CE()
    conf['acl'] = """
        `s1
        `s2, s=1
        `s3
        """

    adv_test.test(module(), conf, verbose=0, duration=120, mass=0)
    #logcat(['cd'])

