if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a.all import *
from slot.d import *

def module():
    return Heinwald

class Heinwald(Adv):
    a1 = ('s',0.4,'hp70')
    a3 = ('prep','100%')
    a3_c = 0.05
    conf = {}
    conf['slots.a'] = RR()+BN()
    conf['slot.d'] = Marishiten()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3
        """

    def init(this):
        if this.condition("buff all teammates"):
            this.s2_proc = this.c_s2_proc

    def prerun(this):
        this.s2ssbuff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')

    def s1_proc(this, e):
        this.skill_charge('s1', this.a3_c)
        
    def c_s2_proc(this, e):
        this.s2ssbuff.on()
        Teambuff('s2team',0.1,10).on()
        Selfbuff('s2self',0.1,10).on()
        this.skill_charge('s2', this.a3_c)

    def s2_proc(this, e):
        this.s2ssbuff.on()
        Selfbuff('s2',0.2,10).on()
        this.skill_charge('s2', this.a3_c)

    def skill_charge(self, proc, c):
        for s in ('s1', 's2', 's3'):
            skill = getattr(self, s)
            skill.charge(skill.sp*c)
            log('sp','{}_charge_{}'.format(proc, s), 0, '{}/{}'.format(int(skill.charged), int(skill.sp)))
    
    def s3_proc(this, e):
        this.skill_charge('s3', this.a3_c)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf,verbose=0, mass=0)

