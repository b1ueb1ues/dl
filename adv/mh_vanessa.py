import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return MH_Vanessa

class MH_Vanessa(Adv):
    a1 = ('fs', 0.30)

    conf = {}
    conf['slot.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['slot.d'] = Corsaint_Phoenix()
    conf['acl'] = """
        #fs=None
        #fs1=this.fs1
        #fs2=this.fs2
        `fs2, s1.charged>=s1.sp-300
        `s1, x=5 or fsc
        `s2, not this.s2_att_boost.get()
        `s3, x=5 or fsc
    """
    conf['cond_afflict_res'] = 0

    def d_slots(this):
        from adv.adv_test import sim_duration
        if sim_duration <= 90:
            this.slots.a = Resounding_Rendition()+The_Chocolatiers()

    def init(this):
        this.conf.fs.hit = 1
        conf_alt_fs = {
            1: {
                'dmg': 143 / 100.0,
                'sp': 100,
                'startup': 41 / 60.0,
                'recovery': 46 / 60.0,
                # 'fs.gauge'       : 150
            },
            2: {
                'dmg': 370 / 100.0,
                'sp': 300,
                'startup': 89 / 60.0,
                'recovery': 46 / 60.0,
                # 'fs.gauge'       : 150
            }
        }
        this.conf['fs1'] = Conf(conf_alt_fs[1])
        this.a_fs1 = Action('fs1', this.conf['fs1'])
        this.a_fs1.atype = 'fs'
        this.a_fs1.interrupt_by = ['s']
        this.a_fs1.cancel_by = ['s','dodge']
        this.l_fs1 = Listener('fs1',this.l_fs1)

        this.conf['fs2'] = Conf(conf_alt_fs[2])
        this.a_fs2 = Action('fs2', this.conf['fs2'])
        this.a_fs2.atype = 'fs'
        this.a_fs2.interrupt_by = ['s']
        this.a_fs2.cancel_by = ['s','dodge']
        this.l_fs2 = Listener('fs2',this.l_fs2)

    def l_fs1(this, e):
        this.a_fs1.getdoing().cancel_by.append('fs1')
        this.a_fs1.getdoing().interrupt_by.append('fs1')
        this.fs_before(e)
        this.update_hits('fs')
        this.dmg_make('fs', this.conf.fs1.dmg, 'fs')
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge('fs1',this.conf.fs1.sp)

    def fs1(this):
        return this.a_fs1()

    def l_fs2(this, e):
        this.a_fs2.getdoing().cancel_by.append('fs2')
        this.a_fs2.getdoing().interrupt_by.append('fs2')
        this.fs_before(e)
        this.update_hits('fs')
        this.dmg_make('fs', this.conf.fs2.dmg, 'fs')
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge('fs2',this.conf.fs2.sp)

    def fs2(this):
        return this.a_fs2()

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

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