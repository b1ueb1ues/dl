import adv_test
import adv
from core.log import *
from slot.a import *

def module():
    return V_Orion

class V_Orion(adv.Adv):

    def init(this):
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)
        this.dmg_make("o_s2_burn",0.803*3)
        this.dc_event = Event('defchain')

    def s2_proc(this, e):
        this.dc_event()


if __name__ == '__main__':
    conf = {}
   # conf['acl'] = """
   #     `s1
   #     `s2
   #     `s3
   #     `fs, seq=3 and cancel
   #     """
   # conf['slots.a'] = First_Rate_Hospitality()+The_Shining_Overlord()

    module().comment = 'no s2'
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3 and cancel
        """
    conf['slots.a'] = The_Shining_Overlord()+LC()
    adv_test.test(module(), conf, verbose=0)

