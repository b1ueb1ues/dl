if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *


def module():
    return Karl

class Karl(adv.Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('a',0.15,'hp70')

    conf = {}
    conf['slot.a'] = The_Shining_Overlord()+Primal_Crisis()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2
        `fs, seq=3
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

