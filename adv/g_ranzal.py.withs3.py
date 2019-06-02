import adv_test
from adv import *
from module.fsalt import *
from slot.a import *
import g_ranzal
from slot import *

def module():
    return G_Ranzal


class sword(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 556
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }


class G_Ranzal(g_ranzal.G_Ranzal):
    comment = "Shining_Overlord+First_Rate_Hospitality ; split 3 alt fs into 2 s1"

    conf = {}
    conf['slots.a'] = The_Shining_Overlord() + First_Rate_Hospitality()
    conf['slots.w'] = sword()


    a3 = ('s',0.3)


    def s3_proc(this, e):
        return


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

