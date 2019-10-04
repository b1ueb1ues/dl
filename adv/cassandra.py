import adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Cassandra(Adv):
    a1 = ('prep','100%')

    def prerun(this):
        timing = adv_test.sim_duration/3
        this.ro(0)
        Timer(this.ro).on(timing)
        Timer(this.ro).on(timing*2)

    def ro(this, t):
        Selfbuff('a3',0.10,-1).on()

if __name__ == '__main__':
    conf = {}
    #conf['slots.a'] = RR()+BN()
    conf['acl'] = """
        `s1
        `s2, seq=5
    """

    adv_test.test(module(), conf, verbose=1)

