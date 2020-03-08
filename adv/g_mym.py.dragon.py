import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
import adv.g_mym

def module():
    return Gala_Mym

class Gala_Mym(adv.g_mym.Gala_Mym):
    conf = adv.g_mym.Gala_Mym.conf.copy()
    conf['acl'] = """
        `dragon.act("c3 c3 s end"), not self.a1_buff.get()
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
    """
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = Resounding_Rendition()+An_Ancient_Oath()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)