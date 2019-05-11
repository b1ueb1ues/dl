import adv_test
import adv
from slot.a import *

def module():
    return Sylas

class Sylas(adv.Adv):
    a3 = ('a',0.13,'hp70')

    comment = 'not consider skill haste for team'

    def init(this):
        this.dmg_make("o_s1_poison",0.582*5)
        this.dmg_make("o_s1_poison",0.582*5)
        this.dmg_make("o_s1_poison",0.582*5)

    def s2_proc(this, e):
        adv.Selfbuff('s2_shaste',0.20,15,'sp','buff').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

