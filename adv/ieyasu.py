if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(Adv):
    a1 = ('cc',0.13,'hp70')
    a2 = ('cd',0.3)

    conf = {}
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """
    conf['cond_afflict_res'] = 0
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+BN()

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static['stacks'] > 0:
                return 0.20
        return 0

    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff("s2",0.20,15,'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Bleed("g_bleed",0).reset()
        this.s2charge = 0
        # if this.conf['cond_afflict_res'] < 100:
        #     from adv.adv_test import sim_duration
        #     if this.condition('always poisoned'):
        #         this.afflics.poison.resist=0
        #         this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration, iv=sim_duration)

    def s1_proc(this, e):
        if this.afflics.poison.get():
            coef = 0.31*8
            this.dmg_make("o_s1_boost", coef)
            Bleed("s1_bleed", 1.752).on()
        else:
            Bleed("s1_bleed", 1.46).on()

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
