import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return MH_Sarisse

class FS_Speedable(Action):
    def __init__(this, name=None, conf=None, act=None):
        super().__init__(name, conf, act)
        this.atype = 'fs'
        this.interrupt_by = ['s']
        this.cancel_by = ['s','dodge']
        this.fs_speed = 1.2
        this.t_fs_speed = Timer(this.fs_speed_off)
        this.l_fs_speed= Listener('fs_speed_buff', this.fs_speed_on)
        this._startup_a = 0

    def fs_speed_on(this, e):
        this.fs_speed = 1.5
        this.t_fs_speed = this.t_fs_speed.on(30)

    def fs_speed_off(this, t):
        this.fs_speed = 1.2

    def sync_config(this, c):
        this._startup_c = c.startup
        this._startup_h = 4 / 60
        this._recovery = 59 / 60
        this._active = c.active

    def getstartup(this):
        startup = this._startup_a
        startup += this._startup_c / this.fs_speed
        startup += this._startup_h / this.speed()
        return startup

    def __call__(this, before):
        if type(before).__name__ == 'FS_Speedable':
            this._startup_a = 88 / 60
        elif type(before).__name__ == 'X':
            if now()-before.startup_start > 0:
                if before.name == 'x1' and this.fs_speed == 1.2:
                    this._startup_a = 3 / 60
                else:
                    this._startup_a = 0
            else:
                return this(before.getprev())
        elif type(before).__name__ == 'S':
            this._startup_a = 0
        elif type(before).__name__ == 'Dodge':
            this._startup_a = 14 / 60
        return this.tap()

class MH_Sarisse(Adv):
    comment = 'fs hit count vary on distance and enemy size; extra hits do 70% less damage than previous hits'
    a1 = ('fs', 0.30)
    a3 = ('fs', 0.25)

    conf = {}
    conf['acl'] = """
        #fs=None
        #fs1=this.fs1
        #fs2=this.fs2
        #fs3=this.fs3
        #fs4=this.fs4
        `s1, fsc
        `s2, fsc
        `dodge, fsc
        `fs4
    """
    conf['slot.a'] = The_Lurker_in_the_Woods()+Dear_Diary()
    conf['slot.d'] = Dragonyule_Jeanne()

    def init(this):
        default_pierce = 2 if this.condition('lance+ distance from HBH sized enemy') else 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 0.74,
                'sp': 500,
                'startup': 29 / 60.0, 
                'recovery': 4 / 60.0,
                'hit': 3,
                'pierce': default_pierce
            },
            'fs2': {
                'dmg': 0.84,
                'sp': 710,
                'startup': (29+43) / 60.0,
                'hit': 3,
                'pierce': default_pierce
            },
            'fs3': {
                'dmg': 0.94,
                'sp': 920,
                'startup': (29+43*2) / 60.0,
                'hit': 4,
                'pierce': default_pierce
            },
            'fs4': {
                'dmg': 1.29,
                'sp': 1140,
                'startup': (29+43*3) / 60.0,
                'hit': 4,
                'pierce': default_pierce
            }
        }
        for n, c in conf_alt_fs.items():
            this.conf[n] = Conf(c)
            act = FS_Speedable(n, this.conf[n])
            this.s2_spd_boost = act.t_fs_speed
            this.__dict__['a_'+n] = act
        
        this.l_fs1 = Listener('fs1',this.l_fs1)
        this.l_fs2 = Listener('fs2',this.l_fs2)
        this.l_fs3 = Listener('fs3',this.l_fs3)
        this.l_fs4 = Listener('fs4',this.l_fs4)

    def do_fs(this, e, name):
        log('fs','succ')
        this.__dict__['a_'+name].getdoing().cancel_by.append(name)
        this.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        this.fs_before(e)
        fs_hits = 0
        for p in range(this.conf[name+'.pierce']):
            coef = this.conf[name+'.dmg']*(0.3**p)
            coef_name = 'fs' if p == 0 else 'o_fs_extra_{}'.format(p)
            if coef < 0.01:
                break
            for _ in range(this.conf[name+'.hit']):
                this.dmg_make(coef_name, coef, 'fs')
                fs_hits += 1
        if name == 'fs4':
            this.hits = fs_hits
        else:
            this.hits += fs_hits
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge(name,this.conf[name+'.sp'])

    def l_fs1(this, e):
        this.do_fs(e, 'fs1')

    def fs1(this):
        doing = this.action.getdoing()
        return this.a_fs1(doing)

    def l_fs2(this, e):
        this.do_fs(e, 'fs2')

    def fs2(this):
        doing = this.action.getdoing()
        return this.a_fs2(doing)

    def l_fs3(this, e):
        this.do_fs(e, 'fs3')

    def fs3(this):
        doing = this.action.getdoing()
        return this.a_fs3(doing)

    def l_fs4(this, e):
        this.do_fs(e, 'fs4')

    def fs4(this):
        doing = this.action.getdoing()
        return this.a_fs4(doing)

    def prerun(this):
        this.s1_fs_boost = adv.SingleActionBuff('s1', 1.00, 1, 'fs', 'buff', ['fs1','fs2','fs3','fs4'])

    def s1_proc(this, e):
        this.s1_fs_boost.on()
    
    def s2_proc(this, e):
        Event('fs_speed_buff')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)