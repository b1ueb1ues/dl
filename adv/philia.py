import adv_test
import adv
from slot.d import *

def module():
    return Philia

class Philia(adv.Adv):
    conf = {}
    a1 = ('a',0.1,'hp100')

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.paralysis.resist=0
        else:
            this.afflics.paralysis.resist=100

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s2_proc(this, e):
        this.afflics.paralysis('s2',90,0.60)


if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Garland()
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)

