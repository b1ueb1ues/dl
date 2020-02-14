import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
import adv.g_mym

def module():
    return adv.g_mym.G_Mym

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `dragon
        `s3, not this.s3_buff_on
        `s1
        `s2, fsc
        `fs, x=5
    """
    conf['slot.a'] = Resounding_Rendition()+An_Ancient_Oath()
    adv.adv_test.test(module(), conf, verbose=0)