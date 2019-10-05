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
    conf = {}
    conf['slots.a'] = RR()+BN()
    conf['acl'] = """
        `s1
        `s2, seq=5
    """

    def prerun(this):
        timing = adv_test.sim_duration/3
        this.ro(0)
        Timer(this.ro).on(timing)
        Timer(this.ro).on(timing*2)
        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

    def ro(this, t):
        Selfbuff('a3',0.10,-1).on()

    def s2_proc(this, e):
        this.dmg_make('o_s2_reflect', this.s2reflect * 11, fixed=True)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

