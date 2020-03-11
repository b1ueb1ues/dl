import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Gala_Euden


class Gala_Euden(Adv):
    comment = 'c2+fs'
    conf = {}
    conf['slot.a'] = The_Shining_Overlord()+SDO()
    conf['slot.d'] = Cupid()
    conf['acl'] = """
        `s1,fsc or s=2
        `s2,fsc
        `s3,fsc
        `fs,seq=2 and cancel
    """
    conf['afflict_res.paralysis'] = 0

    def prerun(self):
        if self.condition('s1 buff for 10s'):
            self.s1on = 1
        else:
            self.s1on = 0
        self.s2.autocharge_init(15873).on()
        if self.condition('draconic charge'):
            self.dragonform.dragon_gauge += 50
        Modifier('a3','dt','hecc',1/0.7-1).on()
        self.dragonlight_spd = Spdbuff('dragonlight',0.1,-1,wide='self')
        Event('dragon').listener(self.a3_on)
        Event('idle').listener(self.a3_off)

    def a3_on(self, e):
        if not self.dragonlight_spd.get():
            self.dragonlight_spd.on()

    def a3_off(self, e):
        if self.dragonlight_spd.get():
            self.dragonlight_spd.off()

    def init(self):
        del self.slots.c.ex['sword']
        self.slots.c.ex['geuden'] = ('ex', 'geuden')

    def s1_proc(self, e):
        if self.s1on :
            Debuff('s1str',-0.20,10,1,'att').on()

    def s2_proc(self, e):
        Event('defchain')()
        self.afflics.paralysis('s2', 120, 0.97)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)