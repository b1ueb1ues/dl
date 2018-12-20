import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikoto21

class Mikoto21(adv.mikoto.Mikoto):
    pass

if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        /s2, seq=5
        /s1, cancel
        /s3, cancel
        """

    adv_test.test(module(), conf, verbose=0)

