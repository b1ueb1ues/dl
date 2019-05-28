import adv_test
from adv import *
from module.fsalt import *
from slot.a import *
import g_ranzal

def module():
    return G_Ranzal


class G_Ranzal(g_ranzal.G_Ranzal):
    comment = "Shining_Overlord+First_Rate_Hospitality ; split 3 alt fs into 2 s1"

    conf = {}
    conf['slots.a'] = The_Shining_Overlord() + First_Rate_Hospitality()


    a3 = ('s',0.3)

    def preconfig(this):
        tmpconf = Conf()
        tmpconf += this.conf_default
        tmpconf += globalconf.get(this.name)
        tmpconf += Conf(this.conf)
        #tmpconf += conf
        tmpconf(this.conf_init)

        tmpconf.slots(tmpconf.slot)

        this.slots.c.att = tmpconf.c.att
        this.slots.c.wt = tmpconf.c.wt
        this.slots.c.stars = tmpconf.c.stars
        this.slots.c.ele = 'water'


        slots_save = slot.Slots()
        slots_save.w = this.slots.w
        slots_save.d = this.slots.d
        slots_save.a = this.slots.a

        this.slot_common = tmpconf.slot_common[0]
        this.slot_common(this.slots)

        if slots_save.w :
            this.slots.w = tmpconf.slots.w
        if slots_save.d :
            this.slots.d = tmpconf.slots.d
        if slots_save.a :
            this.slots.a = tmpconf.slots.a

        if tmpconf.slots.w :
            this.slots.w = tmpconf.slots.w
        if tmpconf.slots.d :
            this.slots.d = tmpconf.slots.d
        if tmpconf.slots.a :
            this.slots.a = tmpconf.slots.a

        this.conf = tmpconf
        this.base_att = this.slots.att(globalconf.forte)
        this.displayed_att = int(this.slots._att(globalconf.forte))
        #this.slots.oninit(this)



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

