if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    a1 = ('prep_charge','5%')
    a3 = ('ro',(0.15, 60))

    conf = {}
    conf['slots.a'] = CC()+TP()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
    """
    conf['cond_afflict_res'] = 0
    def init(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
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

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

