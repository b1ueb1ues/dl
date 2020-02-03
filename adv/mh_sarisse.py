import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return MH_Sarisse

class MH_Sarisse(Adv):
    a1 = ('fs', 0.30)
    a3 = ('fs', 0.25)

    conf = {}
    conf['acl'] = """
        #fs=None
        #fs1=this.fs1
        #fs2=this.fs2
        #fs3=this.fs3
        #fs4=this.fs4
        `s1
        `s2
        `s3
        `dodge, fsc
        `fs4
    """

    def init(this):
        this.conf.fs.hit = 1
        conf_alt_fs = {
            'fs1': {
                'dmg': 0.31*8,
                'sp': 460,
                'startup': 63 / 60.0, 
                'recovery': 37 / 60.0, 
            },
            'fs2': {
                'dmg': 0.31*8,
                'sp': 460,
                'startup': 63 / 60.0, 
                'recovery': 37 / 60.0, 
            },
            'fs3': {
                'dmg': 0.31*8,
                'sp': 460,
                'startup': 63 / 60.0, 
                'recovery': 37 / 60.0, 
            },
            'fs4': {
                'dmg': 0.31*8,
                'sp': 460,
                'startup': 63 / 60.0, 
                'recovery': 37 / 60.0, 
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
        this.l_fs4 = Listener('fs4',this.l_fs4)

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

    def l_fs4(this, e):
        this.do_fs(e, 'fs4')

    def fs4(this):
        return this.a_fs4()

    def prerun(this):
        this.s1_fs_boost = Selfbuff('s1', 1.00, -1, 'fs', 'buff')
        this.s2_spd_boost = Spdbuff('s2', 0, 30) # update this to affect FS start up only???

    def s1_proc(this, e):
        if not this.s1_fs_boost.get():
            this.s1_fs_boost.on()
    
    def s2_proc(this, e):
        this.s2_spd_boost.on()

    def fs_proc(this, e):
        this.s1_fs_boost.off()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


