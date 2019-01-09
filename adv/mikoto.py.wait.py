import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikoto

class Mikoto(adv.mikoto.Mikoto):
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, (seq=5 and cancel or fsc ) and this.s1buff.get() != 0.15
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """
    adv_test.test(module(), conf, verbose=0)


