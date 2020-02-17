import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Hunter_Berserker

class Hunter_Berserker(Adv):
    a1 = ('fs', 0.30)
    conf ={}
    conf['slot.a'] = Levins_Champion()+The_Lurker_in_the_Woods()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `dodge, fsc
        `fs3
        """

    def init(this):
        this.conf.fs.hit = -1
        conf_alt_fs = {
            'fs1': {
                'dmg': 296 / 100.0,
                'sp': 600,
                'startup': (24+39) / 60.0,
                'recovery': 40 / 60.0,
            },
            'fs2': {
                'dmg': 424 / 100.0,
                'sp': 960,
                'startup': (48+40+10) / 60.0,
                'recovery': 40 / 60.0,
            },
            'fs3': {
                'dmg': 548 / 100.0,
                'sp': 1400,
                'startup': (72+40+10) / 60.0,
                'recovery': 40 / 60.0,
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
        this.l_fs3 = Listener('fs3',this.l_fs3)
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

    def l_fs3(this, e):
        this.do_fs(e, 'fs3')

    def fs3(this):
        return this.a_fs3()

    def prerun(this):
        this.s1_debuff = Debuff('s1', 0.05, 10)

        this.s2_fs_boost = SingleActionBuff('s1', 0.80, 1, 'fs', 'buff', ['fs1','fs2','fs3'])

        this.a3_crit = Modifier('a3', 'crit', 'chance', 0)
        this.a3_crit.get = this.a3_crit_get
        this.a3_crit.on()

    def a3_crit_get(this):
        return (this.mod('def') != 1) * 0.20

    def s1_proc(this, e):
        this.s1_debuff.on()

    def s2_proc(this, e):
        this.s2_fs_boost.on(1)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

