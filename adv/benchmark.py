import adv.adv_test
from adv import *
import mikoto

def module():
    return Mikoto

class Mikoto(mikoto.Mikoto):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """


    import cProfile
    p = cProfile.Profile()
    p.enable()
    adv_test.test(module(), conf, verbose=0, mass=1)
    p.print_stats()
