import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(Adv):
    comment = 'no s2'
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = RR()+ADD()
    conf['slots.d'] = Garland()

    def d_acl(this):
        if 'bow' in this.ex:
            this.conf.acl = """
                `s1
                `s3, seq=5 or fsc
                `fs, this.s1.charged>=s1.sp-236
                """



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

