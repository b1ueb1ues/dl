if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot import *

def module():
    return Linyou

class Linyou(Adv):
    comment = '2in1 ' 
    a1 = ('cc',0.10,'hp70')
    a3 = ('sp',0.08)
    conf = {}
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440 
        `s1
        `s2, seq=4
        `s3, seq=5
        """

    def init(this):
        this.conf['slots.d'] = slot.d.wind.Longlong()

    def prerun(this):
        this.s2ssbuff = Selfbuff("s2_s1",1, 10, 'ss','ss')
        this.s2spdbuff = Selfbuff("s2_spd",0.2, 10, 'spd')

    def speed(this):
        if this.s2spdbuff.get():
            return 1.2
        return 1
    

    def s1_proc(this, e):
        if this.s2ssbuff.get():
            this.dmg_make('o_s1_powerup',1.86*3)
            this.s2ssbuff.buff_end_timer.timing += 2.4
            this.s2spdbuff.buff_end_timer.timing += 2.4


    def s2_proc(this, e):
        this.s2ssbuff.on()
        this.s2spdbuff.on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

