import adv_test
import adv
import wep.wand
from core.timeline import *
from core.log import *


def module():
    return Lucretia

class Lucretia(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 3.22*3   ,
        "s1_sp"   : 3530     ,
        "s1_time" : 180/60.0 ,

        "s2_dmg"  : 0        ,
        "s2_sp"   : 4553     ,
        "s2_time" : 109/60.0 ,

        "s3_dmg"  : 4*2.71   ,
        "s3_sp"   : 8597     ,
        "s3_time" : 1        ,
        } )
    conf.update(wep.wand.conf)

    def s2_buff_end(this, e):
        this.buff["s2"] = 1
        log("buff","s2","end   ")


    def double_buff_end(this, e):
        this.buff["double"] = 1
        log("buff","double","end   ")


    def init(this):
        #!!!!!!!!!!!!!!!!!!!!!
        this.s2.charge(400)
        #!!!!!!!!!!!!!!!!!!!!!
        this.energy = 0
        this.s2buff = Event("s2buff",this.s2_buff_end)
        this.doublebuff = Event("doublebuff",this.double_buff_end)
        this.buff = {
                "s2":1,     #1.1 for 10s
                "double":1, #1.2 for 15s
                }

    def att_mod(this):
        return this.buff["s2"] * this.buff["double"]

    def dmg_mod_s(this, name):
        return 1.15*1.25

    def get_energy(this, count):
        this.energy += count
        log("buff","energy",this.energy)
        if this.energy >= 5 :
            this.buff["double"] = 1.2
            this.doublebuff.on(now()+15)
            log("buff","double",'start   ')

    def s1_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s1_energy",this.conf["s1_dmg"]*0.4)
        else:
            this.get_energy(1)
            


    def s2_proc(this, e):
        this.get_energy(2)
        this.buff["s2"] = 1.1
        log("buff","s2","start   ")
        this.s2buff.on(now()+10)


    def s3_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s3_energy",this.conf["s3_dmg"]*0.4)


if __name__ == '__main__':
    conf = {}
    conf['al'] = {
        #'sp': ["s1","s2"],
        'x5': ["s2"],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        's':  ["s3","s2","s1"],
        #'s':  ["s1","s2","s3"],
        } 

    adv_test.test(module(), conf, verbose=0)
    l = logget()
    energized = {'s1':0, 's2':0, 's3':0}
    for i in l:
        if i[1] == 'dmg' and i[2][0] == 's' and i[2][-1:] == 'y':
            energized[i[2][:2]] += i[3]
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
