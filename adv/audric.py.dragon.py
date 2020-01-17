import adv_test
import adv
from adv import *
from core.log import *
from slot.a import *
from slot.d import *
from module.bleed import Bleed
#from module import energy

def module():
    return Audric

class The_Shining_Overlord(Amulet):
    att = 65
    a = [('s',0.40)]

class Audric(adv.Adv):
    comment = 'get 10% dragon charge from enemy every 18s;'
    def prerun(this):

        this.dragonboost = 1.4 # max dragolith

        this.dp = 0
        timing = adv_test.sim_duration/10
        this.t_dp = Timer(this.cb_recoverdp, repeat=1).on(timing)

        this.d = Action('d')
        this.d.conf.startup = 1.8
        this.d.conf.recovery = 12+3.8

        Event('d').listener(this.l_d)

        this.dclaw = 0

        this.bleed = Bleed("g_bleed",0).reset()

        #this.energy = energy.Energy(this, 
         #       self={'1':5},
          #      team={}
           #     )

    def l_d(this, e):
        this.dmg_make('o_d_ss',this.dragonboost*1.5)
        this.dmg_make('o_d_atk',this.dragonboost*35.14)
        this.dmg_make('o_d_skl',this.dragonboost*6.24,'s')
        Bleed("marishiten_bleed", 1.46).on()
        #this.energy.add_energy('1')

    def s1_proc(this, e):
        this.recoverdp(3.45)

    def cb_recoverdp(this,t):
        this.recoverdp(11.5)

    def recoverdp(this, number):
        if this.d.getdoing().name == 'd':
            return
        this.dp += number
        if this.dp > 100:
            this.dp = 100
        log('debug','dp',this.dp)

    def dragon(this):
        if this.dp < 50:
            return 0
        this.dp -= 50

        this.dclaw += 1
        if this.dclaw == 1:
            Selfbuff('dc_1',0.06,-1).on()
        elif this.dclaw == 2:
            Selfbuff('dc_2',0.09,-1).on()
        elif this.dclaw == 3:
            Selfbuff('dc_3',0.15,-1).on()
        
        Selfbuff('a3',0.3,2,'crit','rate').on()
        this.d.getdoing().cancel_by.append('d')
        this.d.getdoing().interrupt_by.append('d')
        this.d()
        return 1

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = The_Shining_Overlord()+BN()
    conf['slot.d'] = Marishiten()
    conf['acl'] = """
        `this.dragon
        `s1
        `s2, fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

