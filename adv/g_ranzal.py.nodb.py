import adv_test
from adv import *
from module.fsalt import *
import g_ranzal

def module():
    return G_Ranzal


class G_Ranzal(g_ranzal.G_Ranzal):
    conf = {}



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, fsc and this.gauges['fs'] > 1000
        `s1, seq=3 and this.fsacharge=3 
        `s1, this.gauges['x'] >=1000 and this.gauges['fs'] >= 1000 and fsc
        `s1, this.gauges['x'] >=1000 and fsc
        `fs, cancel and seq=3 and this.fsacharge > 0
        `fs, cancel and seq=3 and this.fsacharge < 0  
        """



    #conf['slots.a'] = VC() + First_Rate_Hospitality()
    #conf['slots.a'] = VC()+RR()
    adv_test.test(module(), conf, verbose=0, mass=0)

