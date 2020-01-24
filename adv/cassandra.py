import adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    comment = 'no counter damage'
    a1 = ('prep_charge','5%')
    a3 = ('ro',(0.15, 60))

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

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        # this.flurry_str.off()
        this.dmg_make('o_s2_crisis',this.s2boost*10.82)

if __name__ == '__main__':
    conf = {}
    conf['slots.a'] = CC()+TP()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """

    adv_test.test(module(), conf, verbose=-2)

