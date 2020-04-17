import adv.adv_test
from core.advbase import *
from core.log import *
from slot.a import *
from slot.d import *

def module():
    return Valentines_Orion

class Valentines_Orion(Adv):
    conf = {}

    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `fs, seq=2 and cancel
        """
    conf['slots.a'] = Mega_Friends()+EE()
    conf['slots.d'] = Dreadking_Rathalos()
    conf['afflict_res.burn'] = 0

    def prerun(self):
        self.dc_event = Event('defchain')

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)


    def s2_proc(self, e):
        self.dc_event()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

