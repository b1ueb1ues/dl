import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikoto_wait

class Mikoto_wait(adv.mikoto.Mikoto):
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, cancel and this.s1buff != 1.2
        `s2, s=1
        """
    adv_test.test(module(), conf, verbose=0)


