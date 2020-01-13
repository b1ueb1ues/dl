import adv_test
import adv
from slot.a import *

def module():
    return Karina

class Karina(adv.Adv):
    a3 = ('prep','50%')
    conf = Conf()
    conf.slot.a = KFM()+CE()

    def s1_proc(this, e):
        this.dmg_make('o_s1_boost',this.conf['s1.dmg']*0.05*len(this.all_buffs))

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=4
        `s3, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

