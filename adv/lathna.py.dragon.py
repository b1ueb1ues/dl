import adv.adv_test
import adv
from adv import *
from core.log import *
import lathna
from slot.a import *
from slot.d import *

import sys

def module():
    return Lathna

class Lathna(adv.Adv):
    a1 = ('k_poison',0.15)
    conf = {}
    conf['slot.a'] = RR()+The_Plaguebringer()
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        # s1a = this.s1a
        `this.dragon
        `s1a
        `s2, seq = 5
        `s3, seq = 5
        """
    
    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)

        this.afflics.poison.resist=0
        from adv_test import sim_duration
        if this.condition('always poisoned'):
            this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration)

        this.d_k_poison_mod = Modifier('mod_d_k_poison', 'poison_killer', 'hit', 2)
        this.d_k_poison_mod.off()
        
        this.dragonboost = 1.4 # max dragolith

        this.dp = 0
        timing = int(sim_duration/10)
        this.t_dp = Timer(this.cb_recoverdp, repeat=1).on(timing)
        this.comment = 'get 10% dragon charge from enemy every {}s'.format(timing)

        this.d = Action('d')
        this.d.conf.startup = 1.8
        this.d.conf.recovery = 16.28

        Event('d').listener(this.l_d)

    def l_d(this, e):
        this.d_k_poison_mod.on()
        this.dmg_make('o_d_ss',this.dragonboost*1.5)
        this.afflics.poison('s_dragon',120,this.dragonboost*0.291,30)
        this.dmg_make('o_d_skill',this.dragonboost*7.28,'s')
        this.dmg_make('o_d_autos',this.dragonboost*37.61)
        this.d_k_poison_mod.off()

    def cb_recoverdp(this,t):
        this.recoverdp(10)

    def recoverdp(this, number):
        if this.d.getdoing().name == 'd':
            return
        this.dp += number
        if this.dp > 100:
            this.dp = 100
        log('debug','dp',this.dp)

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            with Modifier("s1killer", "poison_killer", "hit", 0.5):
                this.dmg_make("s1", 2.37*4)
            this.conf.s1.recovery = 4.05
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0 
    
    def s1_proc(this, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s1", 2.37*3)

    def s2_proc(this, e):
        with Modifier("s2killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s2", 17.26)

    def dragon(this):
        if this.dp < 50:
            return 0
        this.dp -= 50

        this.d.getdoing().cancel_by.append('d')
        this.d.getdoing().interrupt_by.append('d')
        this.d()
        return 1

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
