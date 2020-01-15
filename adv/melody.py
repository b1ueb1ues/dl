import adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'no s2'
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = LC()+ADD()
    conf['slots.d'] = Garland()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        `fs, seq=5 or this.s1.charged>=s1.sp-200
        """
    adv_test.test(module(), conf, verbose=-2)

