import adv.adv_test
import adv
from adv import *
from core.log import *
from slot.d import *
from slot.a import *

def module():
    return Serena

class Serena(adv.Adv):
    comment = 'Arctos'
    conf = {}
    conf['slot.d'] = Arctos()
    conf['slot.a'] = TSO()+LC()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2,fsc
        `fs, seq=3
        """

    conf = {}
    conf['slot.a'] = TSO()+Primal_Crisis()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2,fsc
        `fs, seq=3
        """

    def s1_before(this, e):
        Selfbuff('s1buff',0.1,5,'crit','rate').on()


    def init(this):
        if this.condition('always connect hits'):
            this.dmg_proc = this.c_dmg_proc


    def prerun(this):
        this.hits = 0
        this.a1count = 0
        this.a3count = 0


    def c_dmg_proc(this, name, amount):
        a1old = this.a1count
        if this.hits > 60:
            this.a1count = 3
        elif this.hits > 40:
            this.a1count = 2
        elif this.hits > 20:
            this.a1count = 1
        if a1old != this.a1count:
            Selfbuff('a1buff',0.06,-1,'crit','damage').on()

        a3old = this.a3count
        if this.hits > 90:
            this.a3count = 3
        elif this.hits > 60:
            this.a3count = 2
        elif this.hits > 30:
            this.a3count = 1
        if a3old != this.a3count:
            Selfbuff('a3buff',0.03,-1,'crit','chance').on()




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

