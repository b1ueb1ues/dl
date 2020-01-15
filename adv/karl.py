import adv_test
import adv
from slot.a import *


def module():
    return Karl

class Karl(adv.Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('a',0.15,'hp70')

    conf = {}
    conf['slot.a'] = The_Shining_Overlord()+Flash_of_Genius()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2
        `s3, fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=-2)

