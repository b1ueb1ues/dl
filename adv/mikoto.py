import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Mikoto

class Mikoto(Adv):
    a1 = ('cc',0.10,'hp70')
    a3 = ('cc',0.08)
    
    conf = {}
    conf['slot.d'] = Arctos()
    conf['acl'] = """
        `s3, x=5 and not this.s3_buff_on
        `s1, x=5
        `s2, x=5
        """

    def prerun(this):
        this.s1buff = Selfbuff("s1",0.0, 20)
        this.s2buff = Spdbuff("s2",0.2, 10)
        this.conf.s1.recovery = 1.4


    def s1latency(this, e):
        this.s1buff.off()
        this.s1buff.on()


    def s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 0:
            stance = 0
        elif buff == 0.10:
            stance = 1
        elif buff == 0.15:
            stance = 2
        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(0.10,20) #.on()
            this.conf.s1.recovery = 1.4
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(0.15,15) #.on()
            this.conf.s1.recovery = 1.63
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 2:
            this.dmg_make('s1',2.13*3+4.25)
            this.s1buff.off().set(0)
            this.conf.s1.recovery = 3.07

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

