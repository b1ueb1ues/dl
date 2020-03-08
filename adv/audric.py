import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Audric

class Audric(Adv):
    a1 = ('dp', 10)
    
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=3
    """
    def prerun(self):
        self.cursed_blood = Selfbuff('cursed_blood',0.30,-1,'crit','chance')
        Event('dragon').listener(self.a3_on)
        Event('idle').listener(self.a3_off)

    def a3_on(self, e):
        if not self.cursed_blood.get():
            self.cursed_blood.on()

    def a3_off(self, e):
        if self.cursed_blood.get():
            self.cursed_blood.off()

    def s1_proc(self, e):
        self.dragonform.charge_gauge(3)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
    # logcat([str(type(module().conf['slot.d']).__name__)])