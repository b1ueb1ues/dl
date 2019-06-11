# encoding:utf8
import adv_test
from adv import *
from slot.a import *

def module():
    return G_Mym

class G_Mym(Adv):


    def init(this):

        this.dragonboost = 1.4 # max 龙哭

        this.dp = 0
        this.truemumu = 0
        timing = adv_test.sim_duration/10
        this.t_dp = Timer(this.cb_recoverdp, repeat=1).on(timing)

        this.d1 = Action('d1')
        this.d2 = Action('d2')
        this.d1.conf.startup = 1.8
        this.d1.conf.recovery = 12+2.5
        this.d2.conf.startup = 1.8
        this.d2.conf.recovery = 12+2.1

        Event('d1').listener(this.l_d1)
        Event('d2').listener(this.l_d2)


    def l_d1(this, e):
        this.dmg_make('o_d_ss',this.dragonboost*1.5)
        this.dmg_make('o_d_atk',this.dragonboost*37.85)
        this.dmg_make('o_d_skl',this.dragonboost*7.56,'s')


    def l_d2(this, e):
        this.dmg_make('o_d_ss',this.dragonboost*1.5)
        this.dmg_make('o_d_atk',this.dragonboost*42.97)
        this.dmg_make('o_d_skl',this.dragonboost*12.18,'s')

    def s1_proc(this, e):
        this.recoverdp(5)

    def s2_proc(this, e):
        if this.truemumu :
            this.dmg_make('o_s2_boost', 4.16)

    def cb_recoverdp(this,t):
        this.recoverdp(10)

    def recoverdp(this, number):
        if this.d1.getdoing().name == 'd1':
            return
        if this.d1.getdoing().name == 'd2':
            return
        this.dp += number
        if this.dp > 100:
            this.dp = 100
        log('debug','dp',this.dp)

    def dragon(this):
        if this.dp < 50:
            return 0
        this.dp -= 50
        if not this.truemumu:
            this.truemumu = 1
            Selfbuff('a1',0.15,-1).on()
            this.d1.getdoing().cancel_by.append('d1')
            this.d1.getdoing().interrupt_by.append('d1')
            this.d1()
        else:
            this.d2.getdoing().cancel_by.append('d2')
            this.d2.getdoing().interrupt_by.append('d2')
            this.d2()
        return 1
    


if __name__ == '__main__':
    conf = {}
#    conf['slot.a'] = RR()+Jewels_of_the_Sun()
#    conf['acl'] = """
#        `this.dragon
#        `s1
#        `s2
#        `s3
#        `fs, seq=5
#        """

    module().comment = 'hold skill after c5; get 10% dp from enemy every 18s;'
    conf['slot.a'] = RR()+CE()
#    import slot
#    conf['slots.d'] = slot.d.flame.Sakuya()

    conf['acl'] = """
        `this.dragon
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)


