import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return G_Euden


class G_Euden(Adv):
    comment = 'c2+fs'
    conf = {}
    conf['slot.a'] = TSO() + SDO()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.paralysis.resist=0
        else:
            this.afflics.paralysis.resist=100

        if this.condition('s1 buff for 10s'):
            this.s1on = 1
        else:
            this.s1on = 0
        if this.condition('get DC at start'):
            Buff('dragonclaw',0.06,-1).on()
            Buff('dragonclaw',0.03,-1).on()
        this.s2timer = Timer(this.s2autocharge,1,1).on()

    def s2autocharge(this, t):
        this.s2.charge(999999.0/63)
        log('sp','s2autocharge')

    def s1_proc(this, e):
        if this.s1on :
            Debuff('s1str',-0.20,10,1,'att').on()

    def s2_proc(this, e):
        Event('defchain')()
        this.afflics.paralysis('s2', 120, 0.97)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `fs,seq=2 and cancel
    """
#    import sys
#    from slot.a import *
#    if len(sys.argv) >= 3:
#        sim_duration = int(sys.argv[2])
#    else:
#        sim_duration = 180
#    if sim_duration == 60:
#        conf['slot.a'] = Choco()+SDO()
#        conf['acl'] = """
#            `s1
#            `s2
#            `fs, seq=2
#            """

    adv_test.test(module(), conf, verbose=-2, mass=0)
