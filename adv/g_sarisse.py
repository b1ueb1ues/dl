import adv.adv_test
import adv
from adv import *
import slot
from slot.a import *

def module():
    return G_Sarisse

class G_Sarisse(adv.Adv):
    a3 = ('bt',0.3)
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, fsc
        `fs, seq=4
    """
    conf['slot.d'] = slot.d.Sakuya()

    def prerun(this):
        this.ahits = 0
        this.bc = adv.Selfbuff()
        this.s2stance = 0

    def dmg_proc(this, name, amount):
        if this.hits // 20 > this.ahits:
            this.ahits = this.hits // 20
            buff = adv.Selfbuff('sylvan strength',0.02,15)
            buff.bufftime = buff.nobufftime
            buff.on()
            buff = adv.Selfbuff('sylvan crit',0.01,15,'crit','chance')
            buff.bufftime = buff.nobufftime
            buff.on()

    def s1_proc(this, e):
        buffcount = min(this.bc.buffcount(), 7)
        this.dmg_make('s1_missile*%d'%buffcount,0.95*buffcount)
        this.hits += buffcount
            
    def s2_proc(this, e):
        if this.s2stance == 0:
            adv.Teambuff('s2str',0.20,10).on()
            this.s2stance = 1
        elif this.s2stance == 1:
            adv.Teambuff('s2def',1,15,'defup').on()
            Event('defchain')()
            this.s2stance = 0


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)