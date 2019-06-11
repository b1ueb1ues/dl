import adv_test
from adv import *
from module.fsalt import *
from slot.a import *

def module():
    return G_Ranzal


class G_Ranzal(Adv):
    comment = "split 3 alt fs into 2 s1"

    conf = {}
    conf['slots.a'] = The_Shining_Overlord() + First_Rate_Hospitality()

    a3 = ('s',0.3)

    def init(this):
        this.ifs1ins2 = 0
        this.gauges = {
                'x':0,
                'fs':0,
                }
        this.fsacharge = -1
        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf({
                'fs.dmg':0.83*2+0.92,
                'fs.sp' :330,
                "fs.startup":33/60.0,
                "fs.recovery":45/60.0,
                "x2fs.startup":18/60.0,
                "x2fs.recovery":45/60.0,
                "x3fs.startup":18/60.0,
                "x3fs.recovery":45/60.0,
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
            this.dmg_make('o_s1_boost',this.conf['s1.dmg']*0.2)
        if boost == 2:
            this.dmg_make('o_s1_boost',this.conf['s1.dmg']*0.8)
        this.ifs1ins2 = 1


    def s2_proc(this, e):
        this.fsacharge = 3
        fs_alt(this)
        this.ifs1ins2 = 0
        Event('defchain')()


    def s3_proc(this, e):
        Event('defchain')()


if __name__ == '__main__':
    conf = {}
    #conf['acl'] = """
    #    `s2, fsc
    #    `s1, seq=3 and this.fsacharge=3 
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000 and fsc
    #    `s1, this.gauges['x'] >=1000 and fsc
    #    `fs, cancel and seq=3 and this.fsacharge > 0
    #    `fs, cancel and seq=3 and this.fsacharge < 0  
    #    """
    #    #`fs, cancel and seq=2 and this.fsacharge < 0 and not ( this.gauges['x']>930 and this.gauges['fs']>1000 )

    #conf['acl'] = """
    #    # fskeep = 0
    #    # if not this.ifs1ins2 and this.fsacharge <= 1 : fskeep = 1 
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
    #    `s2, this.gauges['fs'] >= 300 and this.gauges['fs'] < 800
    #    `fs, cancel and seq=3 and this.fsacharge > 0 and not fskeep and this.gauges['fs'] < 1000
    #    `fs, cancel and seq=2 and this.fsacharge < 0 and this.gauges['x'] >= this.gauges['fs']
    #    `fs, cancel and seq=3 and this.fsacharge < 0 and this.gauges['x'] < this.gauges['fs']
    #    """
    #conf['acl'] = """
    #    # fskeep = 0
    #    # if not this.ifs1ins2 and this.fsacharge <= 1 : fskeep = 1 
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] == 450 and fsc
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] == 650 and fsc
    #    `s2, this.gauges['fs'] >= 300 and this.gauges['fs'] < 800
    #    `fs, cancel and seq=3 and this.fsacharge > 0 and not fskeep and this.gauges['fs'] < 1000
    #    `fs, cancel and seq=3 and this.fsacharge < 0 and this.gauges['x'] >= this.gauges['fs']
    #    `fs, cancel and seq=3 and this.fsacharge < 0 and this.gauges['x'] < this.gauges['fs']
    #    """
    #conf['acl'] = """
    #    `s2, fsc and this.gauges['fs'] > 1000
    #    `s1, seq=3 and this.fsacharge=3 
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000 and fsc
    #    `s1, this.gauges['x'] >=1000 and fsc
    #    `fs, cancel and seq=3 and this.fsacharge > 0
    #    `fs, cancel and seq=3 and this.fsacharge < 0  
    #    """
    #    #`fs, cancel and seq=2 and this.fsacharge < 0 and not ( this.gauges['x']>930 and this.gauges['fs']>1000 )
    #conf['acl'] = """
    #    # fskeep = 0
    #    # if not this.ifs1ins2 and this.fsacharge <= 1 : fskeep = 1 
    #    `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
    #    `s2, this.gauges['fs'] >= 300 and this.gauges['fs'] < 800
    #    `fs, cancel and seq=3 and this.fsacharge > 0 and not fskeep and this.gauges['fs'] < 1000
    #    `fs, cancel and seq=2 and this.fsacharge < 0 and this.gauges['x'] >= this.gauges['fs']
    #    `fs, cancel and seq=3 and this.fsacharge < 0 and this.gauges['x'] < this.gauges['fs']
    #    """
    conf['acl'] = """
        # fskeep = 0
        # if not this.ifs1ins2 and this.fsacharge <= 1 : fskeep = 1 
        `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
        `s2, this.gauges['fs'] >= 300 and this.gauges['fs'] < 800
        `fs, cancel and seq=3 and this.fsacharge > 0 and not fskeep and this.gauges['fs'] < 1000
        `fs, cancel and seq=2 and this.fsacharge < 0 and this.gauges['x'] >= this.gauges['fs']
        `fs, cancel and seq=3 and this.fsacharge < 0 and this.gauges['x'] < this.gauges['fs']
        `s3, fsc
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

