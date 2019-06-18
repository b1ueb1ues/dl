import adv_test
from adv import *
import adv.maribelle
import slot


def module():
    return Maribelle_s3


class Maribelle_s3(adv.maribelle.Maribelle):
    name = 'maribelle'
    conf = {}
    conf['slot.w'] = slot.w.wand5b2p2()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        `s3, s
        """
        
    adv_test.test(module(), conf, verbose=0)

