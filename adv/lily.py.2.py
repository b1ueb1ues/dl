import adv_test
from adv import *
import lily
from slot import *
from slot.a import *



class F(Amulet): # Flash of Genius
    att = 57
    #a = [('a',0.20,'hit15')]

def module():
    return Lily

class Lily(lily.Lily):
    conf = {}
    conf['slot.a'] = RR()+F()
    #conf['slot.a'] = RR()+CE()

    def init(this):
        #this.conf.s2.recovery += 43.0/60*2
        this.fbuff = Selfbuff('f',0.2,-1,'att','passive')
        #this.fbuff = Selfbuff('f',0,-1,'nop')

    def hit(this):
        if this.fbuff.get():
            if this.hits < 15:
                this.fbuff.off()
        elif this.hits >= 15:
            this.fbuff.on()

    def dmg_proc(this, name, amount):
        if name == 'x1_missile':
            this.hits += 1
        elif name == 'x2_missile':
            this.hits += 2
        elif name == 'x3_missile':
            this.hits += 3
        elif name == 'x4_missile':
            this.hits += 2
        elif name == 'x5_missile':
            this.hits += 5
        elif name == 'fs_missile':
            this.hits += 2
        elif name == 's1':
            this.hits = 0
        elif name == 's2':
            this.hits = 0
        this.hit()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        #prep=0
        #if pin=='prep': prep=1
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s2, pin='prep'
        """

    adv_test.test(module(), conf, verbose=0)



