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
        `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000
        `s2, s=1
        `s3, fsc
        `fs, cancel and seq=3 and this.fsacharge > 0
        `fs, cancel and seq=2 and this.fsacharge < 0  
        """
        #`fs, cancel and seq=2 and this.fsacharge < 0 and not ( this.gauges['x']>930 and this.gauges['fs']>1000 )
    from slot.a import *
    conf['slots.a'] = The_Shining_Overlord() + First_Rate_Hospitality()
    #conf['slots.a'] = VC() + First_Rate_Hospitality()
    #conf['slots.a'] = VC()+RR()
    adv_test.test(module(), conf, verbose=0, mass=0)

