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
    conf['slot.a'] = The_Shining_Overlord()+Flash_of_Genius()
    conf['acl'] = """
        `s1, fsc
        `s2
        `s3, fsc
        `fs, seq=3
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

