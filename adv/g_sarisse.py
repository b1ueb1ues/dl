import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Gala_Sarisse

class Gala_Sarisse(Adv):
    a3 = ('bt',0.3)
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = Forest_Bonds()+Dear_Diary()
    conf['acl'] = """
        `s3, fsc and not this.s3_buff
        `s1, cancel
        `s2, fsc
        `fs, seq=4
    """

    def prerun(this):
        this.ahits = 0
        this.bc = Selfbuff()
        this.s2stance = 0

    def dmg_proc(this, name, amount):
        if this.condition('never lose combos'):
            if this.hits // 20 > this.ahits:
                this.ahits = this.hits // 20
                buff = Selfbuff('sylvan strength',0.02,15)
                buff.bufftime = buff.nobufftime
                buff.on()
                buff = Selfbuff('sylvan crit',0.01,15,'crit','chance')
                buff.bufftime = buff.nobufftime
                buff.on()

    def s1_proc(this, e):
        buffcount = min(this.bc.buffcount(), 7)
        this.dmg_make('s1_missile*%d'%buffcount,0.95*buffcount)
        this.hits += buffcount

    def s2_proc(this, e):
        if this.s2stance == 0:
            Teambuff('s2str',0.20,10).on()
            this.s2stance = 1
        elif this.s2stance == 1:
            Teambuff('s2def',0.20,15,'defense').on()
            this.s2stance = 0


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)