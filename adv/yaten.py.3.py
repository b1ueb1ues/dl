if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv
from adv import *
from module import energy
import yaten

def module():
    return Yaten

class Yaten(yaten.Yaten):
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun
            this.conf['acl'] = """
                `s1
                `s2, fsc and this.energy() < 4
                `fs, seq=3
                """
            this.conf['acl'] = """
                `s1, s=2
                `s2, fsc and this.energy() < 4
                `fs, seq=3
                """
        else:
            this.conf['acl'] = """
                `s1
                `fs, seq=3
                """

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'s2':2} ,
                team={'s2':2}
                )
        Event('energized').listener(this.energy_doublebuff)
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()


if __name__ == '__main__':
    conf = {}
    from slot.a import *
    from slot.d import *

    conf['slot.a'] = HoH()+JotS()
    conf['slot.a'] = RR()+JotS()
     
 #   conf['acl'] = """
 #       `s1
 #       `s2, fsc and this.energy() < 4
 #       `fs, seq=3
 #       """

    adv_test.test(module(), conf, verbose=-2)


