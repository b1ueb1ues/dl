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
    att = 333 
    a = [('k',0.3), ('prep','50%')]


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

    conf['acl'] = """
        # from core.timeline import now
        `s1, this.gauges['x'] >=1000 and now()<10
        `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
        `s2, fsc and this.gauges['fs'] >= 300
        `fs, cancel and seq=3 
        `s3, fsc
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

