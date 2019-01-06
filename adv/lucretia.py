import adv_test
import adv
from adv import *

def module():
    return Lucretia

class Lucretia(adv.Adv):
    def init(this):
        #!!!cheat!!!!!!!!!!!!!
        #this.s2.charge(400)
        #!!!!!!!!!!!!!!!!!!!!!
        this.energy = 0
        this.doublebuff = adv.Buff("double", 0.2, 15,'att')

    def add_energy(this, count):
        this.energy += count
        log("buff","energy",this.energy)
        if this.energy >= 5 :
            this.doublebuff.on()

    def s1_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s1_energy",this.conf["s1_dmg"]*0.4)
        else:
            this.add_energy(1)
            

    def s2_proc(this, e):
        this.add_energy(2)


    def s3_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s3_energy",this.conf["s3_dmg"]*0.4)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, sx=2 
        `s1, sx=3
        `s1, seq=5 and cancel
        """

    if 1:
        conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel
            `s3, seq=5 and cancel
            """

    adv_test.test(module(), conf, verbose=0)
    if loglevel >= 0:
        l = logget()
        energized = {'s1':0, 's2':0, 's3':0}
        for i in l:
            if i[1] == 'dmg' and i[2][0] == 's' and i[2][-1:] == 'y':
                energized[i[2][:2]] += i[3]
        for i in energized:
            energized[i] = "%.3f"%energized[i]
        print "energized  |",energized



'''
2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 5 0.| 2 2 3 | 5 0 | 2 2 3 |

2 1 | 2 1 3 | 2 1 | 2 1 3 | 
2 3 | 5 0 0 | 2 3 | 5 0 0 |

2 1 | 2 3 1 | 2 1 | 2 3 1 | 
2 3 | 5 0 1 | 3 4 | 6.0 1 |

2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 1 2 | 3 2 1
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 4 6.| 0 2 3
'''
