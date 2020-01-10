if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    # comment = 'no counter damage'
    a1 = ('prep','100%')
    a1_c = 0.05
    a3 = ('ro',(0.15, 60))

    conf = {}
    conf['slots.a'] = CC()+Dear_Diary()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """
    conf['cond_afflict_res'] = 0
    def init(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

        if this.condition('hp80'):
            this.s2boost = 1.2*0.2*0.2
        else:
            this.s2boost = 1.2*0.3*0.3

    def prerun(this):
        this.comment = 's2 drops combo'
        this.hits = 0

        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        this.dmg_make('o_s2_reflect', this.s2reflect * 11, fixed=True)
        this.dmg_make('o_s2_crisis',this.s2boost*10.82)

    def skill_charge(self, proc, c):
        for s in ('s1', 's2', 's3'):
            if s != proc:
                skill = getattr(self, s)
                skill.charge(skill.sp*c)
                log('sp','{}_charge_{}'.format(proc, s), 0, '{}/{}'.format(int(skill.charged), int(skill.sp)))
    def s1_before(this, e):
        this.skill_charge('s1', this.a1_c)
    def s2_before(this, e):
        this.skill_charge('s2', this.a1_c)
    def s3_before(this, e):
        this.skill_charge('s3', this.a1_c)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

