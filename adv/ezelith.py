import adv.adv_test
from adv import *
from slot.d import *

def module():
    return Ezelith

class Ezelith(Adv):
    comment = ''
    a3 = ('bk',0.35)
    conf = {}
    conf['slot.d'] = Arctos()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, seq=4
        `fs, seq=5
        """


    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff('s2',0.2,15)
        this.s2chance = 0.15
        if this.condition('hp70'):
            this.s2chance += 0.2

    def s1_proc(this, e):
        this.dmg_make('s1',0.63*2,'s')
        this.hits += 2
        Selfbuff('a1',0.2,7.5,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        this.hits += 2
        Selfbuff('a1',0.2,8.0,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        this.hits += 2
        Selfbuff('a1',0.2,8.5,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        this.hits += 2
        Selfbuff('a1',0.2,9.0,'crit','chance').on()
        this.dmg_make('s1',0.63*2,'s')
        this.hits += 2
        Selfbuff('a1',0.2,9.5,'crit','chance').on()
        this.dmg_make('s1',4.00,'s')
        this.hits += 2

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
    adv.adv_test.test(module(), conf, mass=1, verbose=-2)

