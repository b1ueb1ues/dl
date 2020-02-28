import adv.adv_test
from core.advbase import *

def module():
    return Yuya

class Yuya(Adv):
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff
        `s1
        `fs, seq=4
        """

    a3 = ('primed_crit_chance', 0.5,5)

    def prerun(this):
        if this.condition('hp60'):
            Selfbuff('a1',0.2,-1,'att','passive').on()
        else:
            Selfbuff('a1',-0.2,-1,'att','passive').on()

    def s1_proc(this, e):
        Spdbuff("s2",0.2, 10)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

