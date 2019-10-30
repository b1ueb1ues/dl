if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return H_Elisanne

class H_Elisanne(Adv):
    a1 = ('s',0.3)
    conf = {}
    conf['slots.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
        `fs, seq=5
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = HoH()+JotS()

    def prerun(this):
        this.stance = 0

    def s1latency(this, e):
        Teambuff("s1_buff",0.1,15).on()

    def s1_proc(this, e):
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            Timer(this.s1latency).on(2.5)
            this.stance = 2
        elif this.stance == 2:
            Timer(this.s1latency).on(2.5)
            this.stance = 0

    def s2_proc(this, e):
        this.charge('s2',500)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
