import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Delphi

class Twinfold_Bonds(Amulet):  
    att = 65
    a = [('s',0.40)]

class Delphi(Adv):
    a1 = ('a',-0.6)

    def prerun(this):
        this.comment = 's2 drops combo; only use poison FS with combo'
        this.hits = 0
        this.flurry_str = Selfbuff('flurry_str',0.15,-1,'att','passive')
        this.proc_chance = 120
        
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100
        
        if this.condition('s1 defdown for 10s'):
            this.s1defdown = 1
        else:
            this.s1defdown = 0
        
        this.skilltimer = Timer(this.skillautocharge,1,1).on()
        this.s1fscharge = 0

    def skillautocharge(this, t):
        this.s1.charge(999999.0*0.08)
        this.s2.charge(999999.0*0.05)
        log('sp','s1autocharge')

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
            this.hits += 1
        elif name == 's2':
            this.hits += 1
        elif name == 's3':
            this.hits += 5

        if this.hits >= 15:
            this.flurry_str.on()
            this.proc_chance = 180

    def s1_proc(this, e):
        if this.s1defdown :
            Debuff('s1defdown',0.15,10,1).on()
        this.s1fscharge = 1

    def s2_before(this, e):
        this.hits = 0
        this.flurry_str.off()
        this.proc_chance = 120
    
    def s2_proc(this, e):
        this.afflics.poison('s2',this.proc_chance,3.00,24)

    def fs_proc(this, e):
        if this.s1fscharge > 0:
            this.s1fscharge -= 1
            this.dmg_make("o_fs_boost",0.21*3)
            this.afflics.poison('fs',this.proc_chance,3.00,24)

if __name__ == '__main__':
    conf = {}

    conf['slots.a'] = Twinfold_Bonds()+SS()
    conf['slot.d'] = Marishiten()
    conf['acl'] = """
        `s1
        `s2,this.s1fscharge == 0
        `s3
        `fs,seq=2 and cancel and (this.s1fscharge == 0 or this.hits >= 15)
    """

    adv_test.test(module(), conf, verbose=-2, mass=0)
