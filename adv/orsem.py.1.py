import adv_test
from adv import *
from slot.a import *

def module():
    return Orsem

class Orsem(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')


if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+JotS()
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        4C+FS+4C+FS+1C s1
        4C+FS+4C+FS+1C s1
        s2
        4C+FS+4C+FS+1C s3 s1
    """

    adv_test.test(module(), conf, verbose=0, mass=0)

