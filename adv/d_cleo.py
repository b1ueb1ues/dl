import adv_test
import adv
from adv import *

def module():
    return D_Cleo

class D_Cleo(adv.Adv):
    conf = {
        "mod_a": ('att' , 'passive', 0.13) ,
        "mod_d":[('att' , 'passive', 0.45) ,
                 ('crit', 'chance' , 0.20)],
        'condition':'hp70'
        }

    def init(this):
        this.energy = 0

    def add_energy(this, count):
        this.energy += count
        log("buff","energy",this.energy)

    def s1_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s1_energy",this.conf["s1_dmg"]*0.4)
        else:
            this.add_energy(1)
            

    def s2_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s2_energy",this.conf["s2_dmg"]*0.4)


    def s3_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("s3_energy",this.conf["s3_dmg"]*0.4)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
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

