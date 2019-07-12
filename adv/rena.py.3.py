import adv_test
from adv import *
from slot.a import *
from slot.d import *
import rena


def module():
    return Rena

class Rena(rena.Rena):
    comment = ''

if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = RR()+JotS()
    conf['acl'] = """
        `s1
        `s2, s=1
        `fs, seq=5 and s1.charged > s1.sp/2
        `s3, fsc or seq=5
        """
    adv_test.test(module(), conf, verbose=0)

