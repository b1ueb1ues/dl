import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Ezelith

class Elegant_Escort_Always_Burned(Amulet):
    att = 54
    a = [('k',0.3)]

class Ezelith(Adv):
    comment = ''
    a3 = ('bk',0.35)


    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff('s2',0.2,15)
        this.s2chance = 0.15
        if this.condition('hp70'):
            this.s2chance += 0.2

    def s1_proc(this, e):
        this.dmg_make('s1',0.63*2,'s')
        Selfbuff('a1',0.2,7.5,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        Selfbuff('a1',0.2,8.0,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        Selfbuff('a1',0.2,8.5,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        Selfbuff('a1',0.2,9.0,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        Selfbuff('a1',0.2,9.5,'crit','chance').on()
        this.dmg_make('s1',4.00,'s')

    def s2_proc(this, e):
        this.s2buff.on()

    def dmg_proc(this, name, amount):    
        if name[0] != 'x':
            return
        if this.s2buff.get():
            r = random.random()
            if r < this.s2chance:
                Debuff("s2_ab",0.05,5,1).on()


if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Arctos()
    conf['slot.a'] = Elegant_Escort_Always_Burned() + Twinfold_Bonds()
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv.adv_test.test(module(), conf, mass=1, verbose=-2)

