import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(Adv):
    a1 = ('dc', 4)
    a3 = ('dt', 0.25)
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['afflict_res.frostbite'] = 0

    def s1_proc(this, e):
        this.afflics.frostbite('s1',120,0.803)

    def s2_proc(this, e):
        # unknown gauge amount
        this.dragonform.charge_gauge(5)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

