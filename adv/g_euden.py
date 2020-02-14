import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return G_Euden


class G_Euden(Adv):
    comment = 'c2+fs'
    conf = {}
    conf['slot.a'] = The_Chocolatiers()+SDO()
    conf['slot.d'] = Daikokuten()
    conf['acl'] = """
        `s1,fsc or s=2
        `s2,fsc
        `s3,fsc
        `fs,seq=2 and cancel
    """
    conf['afflict_res.paralysis'] = 0

    def prerun(this):
        if this.condition('s1 buff for 10s'):
            this.s1on = 1
        else:
            this.s1on = 0
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        if this.condition('draconic charge'):
            this.dragonform.dragon_gauge += 50
        Modifier('a3','dt','hecc',1/0.7-1).on()

        this.dragonlight_spd = Spdbuff('dragonlight',0.1,-1,wide='self')
        Event('dragon').listener(this.a3_on)
        Event('idle').listener(this.a3_off)

    def a3_on(this, e):
        if not this.dragonlight_spd.get():
            this.dragonlight_spd.on()

    def a3_off(this, e):
        if this.dragonlight_spd.get():
            this.dragonlight_spd.off()

    def init(this):
        del this.slots.c.ex['sword']
        this.slots.c.ex['geuden'] = ('ex', 'geuden')

    def s2autocharge(this, t):
        this.s2.charge(999999.0/63)
        # log('sp','s2autocharge')

    def s1_proc(this, e):
        if this.s1on :
            Debuff('s1str',-0.20,10,1,'att').on()

    def s2_proc(this, e):
        Event('defchain')()
        this.afflics.paralysis('s2', 120, 0.97)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)