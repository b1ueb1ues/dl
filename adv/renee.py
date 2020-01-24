import adv_test
import adv
from adv import *
from slot.a import *

def module():
    return Renee

class Renee(adv.Adv):
    comment = 'no bog'

    a1 = ('primed_crit_chance',(0.6,5))

    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """

    def s2_proc(this, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

