import adv_test
from adv import *
import mikoto
import slot

def module():
    return Mikoto

class Mikoto(mikoto.Mikoto):

    def pre(this):
        this.conf['slots.w'] = slot.w.blade.bladev5flame()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

