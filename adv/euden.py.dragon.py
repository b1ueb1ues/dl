import adv.adv_test
import adv
from adv import *
from core.log import *
import euden
from slot.a import Amulet, Elegant_Escort
from slot import DragonBase

import sys

class The_Shining_Overlord(Amulet):
    att = 65
    a = [('s',0.40), ('dc_true', 3)]

def module():
    return Euden

class DragonForm(Action):
    def __init__(this, name, conf, adv, ds_proc=None, timing=None):
        this.name = name
        this.conf = conf
        this.adv = adv
        this.ds_proc = ds_proc
        this.has_skill = True
        this.act_list = []
        for a in this.conf.act.split(' '):
            if a[0] == 'c' or a[0] == 'x':
                for i in range(1, int(a[1])+1):
                    dxseq = 'dx{}'.format(i)
                    if dxseq in this.conf:
                        this.act_list.append(dxseq)
            elif a == 's' or a == 'ds':
                this.act_list.append('ds')
            elif a == 'end':
                this.act_list.append('end')

        this.action_timer = None

        shift_time = this.conf.dshift.startup + this.conf.duration
        this.shift_end_timer = Timer(this.d_shift_end, timeout=shift_time)
        this.idle_event = Event('idle')

        this.c_act_name = None
        this.c_act_conf = None
        this.dracolith_mod = this.adv.Modifier('dracolith', 'att', 'hit', this.conf.dracolith)
        this.dracolith_mod.off()

        this.dragon_gauge = 0
        if timing is None:
            from adv.adv_test import sim_duration
            timing = int(sim_duration/10)
        this.dragon_gauge_timer = Timer(this.auto_gauge, repeat=1).on(timing)

    def auto_gauge(this, t):
        this.charge_gauge(10)

    def charge_gauge(this, value):
        if this.adv.slots.c.wt == 'sword':
            this.dragon_gauge += value*1.15
        else:
            this.dragon_gauge += value
        this.dragon_gauge = min(this.dragon_gauge, 100)
        log('dragon', 'gauge', '{}% / 100'.format(this.dragon_gauge))

    def d_shift_end(this, t):
        log('dragon', 'end', this.shift_end_timer.timing)
        this.dracolith_mod.off()
        this.has_skill = True
        this.status = -2
        this._setprev() # turn this from doing to prev
        this._static.doing = this.nop
        this.idle_event()

    def d_act_start(this, name):
        if this._static.doing == this and this.action_timer is None:
            prev_act = this.c_act_name
            prev_conf = this.c_act_conf
            this.c_act_name = name
            this.c_act_conf = this.conf[name]
            if this.c_act_name == 'ds' and prev_act is not None:
                this.action_timer = Timer(this.d_act_do, this.c_act_conf.startup-prev_conf.recovery).on()
            else:
                this.action_timer = Timer(this.d_act_do, this.c_act_conf.startup).on()

    def d_act_do(this, t):
        this.adv.hits += this.c_act_conf.hit
        if this.c_act_name == 'ds':
            this.has_skill = False
            this.shift_end_timer.timing += this.conf.ds.startup
            this.ds_proc()
        else:
            this.adv.dmg_make('o_d_'+this.c_act_name, this.c_act_conf.dmg)
        this.action_timer = Timer(this.d_act_next, this.c_act_conf.recovery).on()
    
    def d_act_next(this, t):
        this.action_timer = None
        if len(this.act_list) > 0:
            nact = this.act_list.pop(0)
            if nact == 'end':
                this.shift_end_timer.off()
                this.d_shift_end(None)
            else:
                this.d_act_start(nact)
        elif this.c_act_name[0:2] == 'dx':
            nx = 'dx{}'.format(int(this.c_act_name[2])+1)
            if nx in this.conf:
                this.d_act_start(nx)
            else:
                if this.has_skill:
                    this.d_act_start('ds')
                else:
                    this.d_act_start('dx1')
        else:
            this.d_act_start('dx1')

    def __call__(this):
        if this.dragon_gauge < 50:
            return False
        else:
            this.dragon_gauge -= 50
            this.has_skill = True
            this.status = -1
            this._setdoing()
            this.shift_end_timer.on()
            this.dracolith_mod.on()
            # this.adv.shift_proc() for weird interactions
            Event('dragon')()
            this.d_act_start('dshift')
            return True

class Apollo(DragonBase):
    ele = 'flame'
    att = 127
    a = [('k_burn', 0.2), ('a', 0.5)]
    dragonform = {
        'duration': 600 / 60, # 10s dragon time
        'dracolith': 0.40,
        'act': 'c3 s',

        'dshift.startup': 96 / 60, # shift 102 -> 96 + 6
        'dshift.recovery': 6 / 60,
        'dshift.dmg': 2.00,
        'dshift.hit': 1,

        'dx1.dmg': 1.90,
        'dx1.startup': 23 / 60.0, # c1 frames
        'dx1.recovery': 36 / 60.0, # c2 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.09,
        'dx2.startup': 0,
        'dx2.recovery': 35 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 2.57,
        'dx3.startup': 0,
        'dx3.recovery': 40 / 60.0, # dodge frames
        'dx3.hit': 1,

        'ds.startup': 110 / 60, # skill frames
        'ds.recovery': 0,
        'ds.hit': 2,
    }

    def oninit(self, adv):
        DragonBase.oninit(self, adv)
        self.adv = adv
        self.adv.dform = DragonForm(type(self).__name__, Conf(self.dragonform), adv, self.ds_proc)
    
    def ds_proc(self):
        self.adv.dmg_make('o_d_ds',1.80)
        Debuff('ds',0.05,10).on()
        self.adv.afflics.burn('ds',120,0.311,30,dtype='s')
        self.adv.dmg_make('o_d_ds',4.20)

class Euden(adv.Adv):
    a1 = ('dc_true', 4)
    conf = {}
    conf['slot.d'] = Apollo()
    conf['slot.a'] = The_Shining_Overlord()+Elegant_Escort()
    conf['acl'] = """
        #dragon=this.dform
        `dragon, cancel
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.dform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)