import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikotobad

class Mikotobad(adv.mikoto.Mikoto):
    pass

if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        `s1
        `s3
        `s2
        `fs, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0)

