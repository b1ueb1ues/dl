class C(object):
    pass

class A(object):
    def foo(this, k, v):
        if k == 'k1':
            this.k1 = v
        elif k == 'k2':
            this.k2 = v

    def foo2(this, c):
        this.k1 = c.k1
        this.k2 = c.k2

    def test1(this):
        #this.foo = None
        for i in range(1000000):
            this.foo('k1', 1)
            this.foo('k2', 2)

    def test2(this):
        c = C()
        c.k1 = 1
        c.k2 = 2
        for i in range(1000000):
            this.foo2(c)
            this.foo2(c)
    
a = A()
a2 = A()

import cProfile
p = cProfile.Profile()
p.enable()

a.test1()
a2.test2()

p.print_stats()
exit()


import adv_test
from adv import *
import mikoto

def module():
    return Mikoto

class Mikoto(mikoto.Mikoto):
    conf = {
        "mod_a2"  : ('crit' , 'chance'  , 0.08) ,
        }
    def pre(this):
        if this.condition('hp70'):
            this.conf['mod_a'] = ('crit' , 'passive', 0.10)
        if this.condition('connect s1'):
            this.s1_proc = this.c_s1_proc

    def init(this):
        this.s1buff = Selfbuff("s1",0.0, 15)
        this.s2buff = Selfbuff("s2",0.2, 10, 'spd')

    def speed(this):
        return 1+this.s2buff.get()
    
    def s1latency(this, e):
        this.s1buff.on()

    def s1_proc(this, e):
        this.s1buff.off()
        this.dmg_make('s1',5.32*2)
        this.s1buff.set(0.10).on()
        Timer(this.s1latency).on(1.5/this.speed())

    def c_s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 0:
            stance = 0
        elif buff == 0.10:
            stance = 1
        elif buff == 0.15:
            stance = 2
        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(0.10) #.on()
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(0.15) #.on()
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.s1buff.off().set(0)

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """


    import cProfile
    p = cProfile.Profile()
    p.enable()
    adv_test.test(module(), conf, verbose=0, mass=1)
    p.print_stats()
