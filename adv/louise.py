import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Louise

class Louise(Adv):
    a1 = ('od',0.13)
    comment = 'no fs'
    conf = {}
    conf['slot.a'] = Dear_Diary() + The_Fires_of_Hate()
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        """
    conf['afflict_res.poison'] = 0

    def s1_proc(this, e):
        this.afflics.poison('s1', 120, 0.582)


    def s2_proc(this, e):
        with Modifier("s2killer", "poison_killer", "hit", 0.5):
            this.dmg_make("s2", 8.07)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
