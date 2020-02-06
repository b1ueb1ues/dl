import adv.adv_test
import adv
from adv import *
from core.log import *
import euden
from slot.a import Amulet, Elegant_Escort
from slot.d import *

import sys

class The_Shining_Overlord(Amulet):
    att = 65
    a = [('s',0.40)]

def module():
    return Euden

def d_s_cerberus(this):
    Debuff('cerberus',0.05,10).on()
    this.afflics.burn('s_dragon',120,this.dragonboost*0.97)
    this.dmg_make('o_d_skill',this.dragonboost*7.70,'s')

def d_s_apollo(this):
    Debuff('apollo',0.05,10).on()
    this.afflics.burn('s_dragon',120,this.dragonboost*0.311,30)
    this.dmg_make('o_d_skill',this.dragonboost*5.40,'s')

def d_s_arctos(this):
    this.dmg_make('o_d_skill',this.dragonboost*10,'s')

def d_s_sakuya(this):
    this.dmg_make('o_d_skill',this.dragonboost*6.60,'s')
    this.sd_boost = 1

dragon_confs = {
    'Cerberus': {
        'slot.d': Cerberus,
        #'autos': 35,
        'autos': 7,
        'skill': d_s_cerberus,
        #'recovery': 15.52
        'recovery': 1.08+2.2+4.4
    },
    'Apollo': {
        'slot.d': Apollo,
        # 'autos': 32.80,
        'autos': 6.56,
        'skill': d_s_apollo,
        # 'recovery': 12.98
        'recovery': 1.08+2.2+2
    },
    'Arctos': {
        'slot.d': Arctos,
        #'autos': 40.53,
        'autos': 12.81,
        'skill': d_s_arctos,
        #'recovery': 13.93
        'recovery': 1.08+3.2+3.25
    },
    'Sakuya': {
        'slot.d': Sakuya,
        # 'autos': 33.44,
        'autos': 8.13,
        'skill': d_s_sakuya,
        # 'recovery': 13.75
        'recovery': 1.08+3+2.85
    }
}

class Euden(adv.Adv):    
    conf = {}
    conf['dragonform'] = 'Apollo'
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        `this.dragon
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, seq=3 and cancel
        """

    def d_slots(this):
        this.dragon_config = dragon_confs[this.conf['dragonform']]
        this.conf.slot.d = this.dragon_config['slot.d']()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100
        this.dragonboost = 1.4 # max dragolith

        this.dp = 0
        from adv.adv_test import sim_duration
        timing = int(sim_duration/10)
        this.t_dp = Timer(this.cb_recoverdp, repeat=1).on(timing)
        this.comment = 'get 10% dragon charge from enemy every {}s; end dragon after C3+Skill'.format(timing)

        this.d = Action('d')
        this.d.conf.startup = 1.8
        this.d.conf.recovery = this.dragon_config['recovery']

        this.d_skill = this.dragon_config['skill']

        Event('d').listener(this.l_d)

        this.dclaw = 0
        this.sd_boost = 0

    def l_d(this, e):
        this.dmg_make('o_d_ss',this.dragonboost*2.0)
        this.d_skill(this)
        this.dmg_make('o_d_autos',this.dragonboost*this.dragon_config['autos'])

    def cb_recoverdp(this,t):
        this.recoverdp(11.5)

    def recoverdp(this, number):
        if this.d.getdoing().name == 'd':
            return
        this.dp += number
        if this.dp > 100:
            this.dp = 100
        log('debug','dp',this.dp)

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.recoverdp(5.75)
        this.d_s_sakuya_sd_boost('s1')

    def s2_proc(this, e):
        this.d_s_sakuya_sd_boost('s2')

    def s3_proc(this, e):
        this.d_s_sakuya_sd_boost('s3')

    def d_s_sakuya_sd_boost(this, name):
        if this.sd_boost == 1:
            this.sd_boost = 0
            this.dmg_make('o_s_sakuya_boost',this.conf['{}.dmg'.format(name)]*0.4,'s')

    def dragon(this):
        if this.dp < 50:
            return 0
        this.dp -= 50

        this.dclaw += 1
        if this.dclaw == 1:
            Selfbuff('dc_1_print',0.06,-1).on()
            Selfbuff('dc_1_euden',0.10,-1).on()
        elif this.dclaw == 2:
            Selfbuff('dc_2_print',0.09,-1).on()
            Selfbuff('dc_2_euden',0.15,-1).on()
        elif this.dclaw == 3:
            Selfbuff('dc_3_print',0.15,-1).on()
            Selfbuff('dc_3_euden',0.15,-1).on()

        this.d.getdoing().cancel_by.append('d')
        this.d.getdoing().interrupt_by.append('d')
        this.d()
        return 1

if __name__ == '__main__':
    conf = {}
    dra = 'Sakuya'

    if dra in dragon_confs:
        conf['dragonform'] = dra
        adv.adv_test.test(module(), conf)
    else:
        for dra in dragon_confs:
            conf['dragonform'] = dra
            adv.adv_test.test(module(), conf)