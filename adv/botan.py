import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Botan

class Botan(Adv):
#    comment = "RR+Jewels"
    a3 = ('prep','100%')
    a3_c = 0.05
    conf = {}
    conf['slots.a'] = RR() + BN()
    conf['slots.d'] = Shinobi()

    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
    
    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        Bleed("s1_bleed", 1.44).on()

    def c_s2_proc(this, e):
        Teambuff('s2',0.1,15,'crit','chance').on()

    def s2_proc(this, e):
        Selfbuff('s2',0.1,15,'crit','chance').on()

    def skill_charge(self, proc, c):
        for s in ('s1', 's2', 's3'):
            if s != proc:
                skill = getattr(self, s)
                skill.charge(skill.sp*c)
                log('sp','{}_charge_{}'.format(proc, s), 0, '{}/{}'.format(int(skill.charged), int(skill.sp)))
    def s1_before(this, e):
        this.skill_charge('s1', this.a3_c)
    def s2_before(this, e):
        this.skill_charge('s2', this.a3_c)
    def s3_before(this, e):
        this.skill_charge('s3', this.a3_c)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, pin='prep'
        `s2
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=-2,mass=0)


