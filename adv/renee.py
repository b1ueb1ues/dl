import adv.adv_test
import adv
from adv import *
from slot.a import *

def module():
    return Renee

class Renee(adv.Adv):
    a1 = ('primed_crit_chance',(0.6,5))

    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    conf['afflict_res.bog'] = 100

    def s1_proc(this, e):
        this.dmg_make('s1',1.11)
        this.afflics.bog.on('s1', 100)
        this.dmg_make('s1',5.55)

    def s2_proc(this, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

