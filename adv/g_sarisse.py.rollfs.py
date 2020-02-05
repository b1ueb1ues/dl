import adv.adv_test
from slot.a import *
from slot.d import *
import adv.g_sarisse

def module():
    return G_Sarisse

class G_Sarisse(adv.g_sarisse.G_Sarisse):
    comment = 'roll fs'
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1,fsc
        `s2,fsc
        `dodge, fsc
        `fs
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

