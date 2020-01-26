import adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    comment = 'no counter damage; s2 drops combo'
    a1 = ('prep_charge','5%')
    a3 = ('ro',(0.15, 60))

    conf = {}
    conf['slots.a'] = CC()+TP()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """

    def init(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

    def prerun(this):
        this.hp = 80

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        with CrisisModifier('s2', 2, this.hp):
            this.dmg_make('o_s2_crisis',this.conf.s2.dmg)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

