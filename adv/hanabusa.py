import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Hanabusa

class Hanabusa(Adv):

    def prerun(this):
        this.stance = 0

    def s1_proc(this, e):
        if this.stance == 0:
            this.s1.sp = 2567
            this.stance = 1
            Timer(this.stanceend).on(20)
        elif this.stance == 1:
            this.dmg_make('s1',1.94)
            this.stance = 2
            Timer(this.stanceend).on(20)
        elif this.stance == 2:
            this.dmg_make('s1',2.51)
            this.s1.sp = 2840
            this.stance = 0

    def s2_proc(this, e):
        if this.stance == 0:
            Teambuff('s2',0.15,15).on()
        elif this.stance == 1:
            Teambuff('s2',0.15,18).on()
        elif this.stance == 2:
            Teambuff('s2',0.15,21).on()

    def stanceend(this, e):
        this.s1.sp = 2840
        this.stance = 0

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=-2)

