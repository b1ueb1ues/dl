import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Hunter_Vanessa

class Hunter_Vanessa(Adv):
    a1 = ('fs', 0.30)

    conf = {}
    conf['slot.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['slot.d'] = Corsaint_Phoenix()
    conf['acl'] = """
        `fs2, s1.charged>=s1.sp-this.sp_val('fs2')
        `s1, x=5 or fsc
        `s2, not this.s2_att_boost.get()
        `s3, x=5 or fsc
    """
    conf['afflict_res.paralysis'] = 0

    def d_slots(this):
        from adv.adv_test import sim_duration
        if sim_duration <= 90:
            this.slots.a = Resounding_Rendition()+The_Chocolatiers()

    def init(this):
        this.conf.fs.hit = 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 143 / 100.0,
                'sp': 100,
                'startup': 41 / 60.0,
                'recovery': 46 / 60.0,
                # 'fs.gauge'       : 150
            },
            'fs2': {
                'dmg': 370 / 100.0,
                'sp': 300,
                'startup': 89 / 60.0,
                'recovery': 46 / 60.0,
                # 'fs.gauge'       : 150
            }
        }
        for n, c in conf_alt_fs.items():
            this.conf[n] = Conf(c)
            act = Action(n, this.conf[n])
            act.atype = 'fs'
            act.interrupt_by = ['s']
            act.cancel_by = ['s','dodge']
            this.__dict__['a_'+n] = act
        
        this.l_fs1 = Listener('fs1',this.l_fs1)
        this.l_fs2 = Listener('fs2',this.l_fs2)
        this.fs = None

    def do_fs(this, e, name):
        log('fs','succ')
        this.__dict__['a_'+name].getdoing().cancel_by.append(name)
        this.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        this.fs_before(e)
        this.update_hits('fs')
        this.dmg_make('fs', this.conf[name+'.dmg'], 'fs')
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge(name,this.conf[name+'.sp'])

    def l_fs1(this, e):
        this.do_fs(e, 'fs1')

    def fs1(this):
        return this.a_fs1()

    def l_fs2(this, e):
        this.do_fs(e, 'fs2')

    def fs2(this):
        return this.a_fs2()

    def prerun(this):
        this.s2_att_boost = Selfbuff('s2', 0.30, 90, 'att', 'buff')

        this.a3_crit = Modifier('a3', 'crit', 'chance', 0)
        this.a3_crit.get = this.a3_crit_get
        this.a3_crit.on()

        this.fs_debuff = Debuff('fs',0.05,15)

    def a3_crit_get(this):
        return (this.mod('def') != 1) * 0.20

    def s1_proc(this, e):
        this.afflics.paralysis('s1',120, 0.97)

    def s2_proc(this, e):
        this.s2_att_boost.on()

    def fs_proc(this, e):
        if e.name == 'fs2':
            this.fs_debuff.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)