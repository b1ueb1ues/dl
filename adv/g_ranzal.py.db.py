import adv_test
from adv import *
from module.fsalt import *
import g_ranzal

def module():
    return G_Ranzal


class G_Ranzal(g_ranzal.G_Ranzal):
    comment = "Shining_Overlord+First_Rate_Hospitality ; without lowen's def"
    def s2_proc(this, e):
        g_ranzal.G_Ranzal.s2_proc(this, e)
        Event('defchain')()


    def s3_proc(this, e):
        g_ranzal.G_Ranzal.s3_proc(this, e)
        Event('defchain')()



if __name__ == '__main__':
    conf = {}
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

    from slot.a import *
    conf['slots.a'] = The_Shining_Overlord() + First_Rate_Hospitality()
    #conf['slots.a'] = VC() + First_Rate_Hospitality()
    #conf['slots.a'] = VC()+RR()
    adv_test.test(module(), conf, verbose=0, mass=0)

