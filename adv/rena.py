if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *
from slot.w import *


def module():
    return Rena

class Rena(Adv):
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = VC()+EE()
    conf['acl'] = """
        `s3, cancel
        `s1
        `s2, s=1
        `fs, seq=5 and (s1.charged=1500 or s1.charged=3200)
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

        this.a1_iscding = 0
        this.stance = 0

    def s1_proc(this, e):
        this.dmg_make("s1", 0.72)
        this.afflics.burn('s1',120,0.97)
        this.dmg_make("s1", 0.72*3 + 6.65)

        if this.stance == 0:
            this.stance = 1
            this.dmg_make("o_s1_hit1", 0.72)
            this.afflics.burn('s1',120,0.97)
            this.dmg_make("o_s1_laterhits", 8.81)

        elif this.stance == 1:
            this.stance = 2
            this.dmg_make("o_s1_hit1", 0.72)
            this.afflics.burn('s1',120,0.97)
            this.dmg_make("o_s1_laterhits", 8.81)
            Selfbuff('s1crit',0.1,15,'crit','chance').on()

        elif this.stance == 2:
            this.stance = 0
            with Modifier("s1killer", "burn_killer", "hit", 0.8):
                this.dmg_make("o_s1_hit1", 0.72)
                this.afflics.burn('s1',120,0.97)
                this.dmg_make("o_s1_laterhits", 8.81)
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
            coef = this.afflics.burn.get()*9.53*0.8
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
   # conf['slot.a'] = RR()+FRH()
    conf['slot.a'] = RR()+EE()
    conf['acl'] = """
        `s1
        `s2, s=1
        `s3, not this.s3_buff_on
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0, mass=0)
    #logcat(['cd'])
