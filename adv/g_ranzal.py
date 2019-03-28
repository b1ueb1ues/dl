import adv_test
from adv import *
from module.fsalt import *

def module():
    return G_Ranzal


class G_Ranzal(Adv):
    conf = {
        "mod_a3": ('s', 'passive', 0.3),
        } 


    def init(this):
        this.gauges = {
                'x':0,
                'fs':0,
                }
        this.fsacharge = -1
        this.fsaconf = copy.deepcopy(this.conf)
        this.fsaconf.update({
                'fs_dmg':0.83*2+0.92,
                'fs_sp' :330,
                "fs_startup":33/60.0,
                "fs_recovery":33/60.0,
                "x2fs_startup":18/60.0,
                "x2fs_recovery":33/60.0,
                "x3fs_startup":18/60.0,
                "x3fs_recovery":33/60.0,
                })
        fs_alt_init(this, this.fsaconf)

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.gauges['x'] += 77
        elif name == 'x2':
            this.gauges['x'] += 77
        elif name == 'x3':
            this.gauges['x'] += 100
        elif name == 'x4':
            this.gauges['x'] += 136
        elif name == 'x5':
            this.gauges['x'] += 200
        elif name == 'fs':
            this.gauges['fs'] += 150
        elif name == 'o_fs_alt':
            this.gauges['fs'] += 350
        log('debug','gauges',"%d, %d"%(this.gauges['x'],this.gauges['fs']), \
            "%d, %d"%(this.gauges['x'],this.gauges['fs']))

    def fs_proc(this, e):
        if this.fsacharge > 0:
            this.fsacharge -= 1
            if this.fsacharge == 0:
                fs_back(this)
                this.fsacharge = -1

    def s1_proc(this, e):
        boost = 0
        if this.gauges['x'] >= 1000:
            boost += 1
            this.gauges['x'] = 0
        if this.gauges['fs'] >= 1000:
            boost += 1
            this.gauges['fs'] = 0
        if boost == 1:
            this.dmg_make('o_s1_boost',this.conf['s1_dmg']*0.2)
        if boost == 2:
            this.dmg_make('o_s1_boost',this.conf['s1_dmg']*0.8)

    def s2_proc(this, e):
        this.fsacharge = 3
        fs_alt(this)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
        `s2, s=1
        `fs, cancel and seq=3 and this.fsacharge > 0
        `fs, cancel and seq=2 and this.fsacharge < 0  
        """
        #`fs, cancel and seq=2 and this.fsacharge < 0 and not ( this.gauges['x']>930 and this.gauges['fs']>1000 )
    adv_test.test(module(), conf, verbose=0, mass=0)

