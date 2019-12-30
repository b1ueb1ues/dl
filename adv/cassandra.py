import adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Flash_of_Genius(Amulet):
    att = 57

class Cassandra(Adv):
    comment = 'no counter damage'
    a1 = ('prep','100%')
    a1_c = 0.05
    a3 = ('ro',0.15)

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
        this.flurry_str = Selfbuff('flurry_str',0.2,-1,'att','passive')
        
        #timing = adv_test.sim_duration/3
        #this.ro(0)
        #Timer(this.ro).on(timing)
        #Timer(this.ro).on(timing*2)

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.hits += 1
        elif name == 'x2':
            this.hits += 2
        elif name == 'x3':
            this.hits += 3
        elif name == 'x4':
            this.hits += 2
        elif name == 'x5':
            this.hits += 5
        elif name == 'fs':
            this.hits += 2
        elif name == 's1':
            this.hits += 2
        elif name == 's2':
            this.hits += 5
        elif name == 's3':
            this.hits += 1

        if this.hits >= 15:
            this.flurry_str.on()

    #def ro(this, t):
        #Selfbuff('a3',0.10,-1).on()

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        this.flurry_str.off()
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
    conf['slots.a'] = CC()+Flash_of_Genius()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """

    adv_test.test(module(), conf, verbose=-2)

