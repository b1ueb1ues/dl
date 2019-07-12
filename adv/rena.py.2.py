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
    module().comment = 'Sakuya'
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = RR()+FRH()
    conf['acl'] = """
        `s1
        `s2, s=1
        `s3, seq=5
        """

    adv_test.test(module(), conf, verbose=0)

