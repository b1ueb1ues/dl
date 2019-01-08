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
        this.stance = 0
        this.energy = 0
        this.hits = 0

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.hits += 1
        elif name == 'x2':
            this.hits += 2
        elif name == 'x3':
            this.hits += 2
        elif name == 'x4':
            this.hits += 1
        elif name == 'x5':
            this.hits += 1
        elif name == 'fs':
            this.hits += 3
        elif name == 's1':
            this.hits += 11
        elif name == 's2':
            this.hits += 5
        if this.hits >= 30:
            this.add_energy(1)
            this.hits -= 30

    def add_energy(this, count):
        this.energy += count
        log("buff","energy",this.energy)

    def s1_proc(this, e):
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
            adv.Buff('s1s',0.1,10,'att').on()
        elif this.stance == 2:
            this.stance = 0
            adv.Buff('s1s',0.1,10,'att').on()
            adv.Buff('s1c',0.08,10,'crit','chance').on()

        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("o_s1_energy",this.conf["s1_dmg"]*0.4)
        else:
            this.add_energy(1)
            

    def s2_proc(this, e):
        if this.energy >= 5:
            this.energy = 0
            log("buff","energy",this.energy)
            this.dmg_make("o_s2_energy",this.conf["s2_dmg"]*0.4)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0)
