import adv_test
import adv
import veronica
import slot.a
from slot import *


def module():
    return Veronica

class Veronica(veronica.Veronica):
    comment = '1hp; only c5 & s1;'
    a3 = ('prep','100%')
    conf = {}
    conf['slots.a'] = slot.a.FG() + slot.a.Heralds_of_Hinomoto()

    def pre(this):
        if this.condition('hp1'):
            this.s1boost = 1.25
        else:
            this.s1boost = 0

    def s1_proc(this, e):
        if this.s1boost:
            this.dmg_make('o_s1_crisis', this.s1boost*10.84)


if __name__ == '__main__':
    conf = {}
#    conf['acl'] = """
#        `s1, seq=5 and cancel or fsc
#        `s1, pin == 'prep'
#        `fs, seq=5 and s1.charged >= 2500
#        """

    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

