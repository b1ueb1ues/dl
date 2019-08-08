import adv.adv_test
from adv import *
import mikoto
import albert
from slot.d import *

def module():
    return Benchmark

class Benchmark(albert.Albert):
    name = 'albert'
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1, this.s2.charged > 900
        `s3
        `fs, seq=2 and not this.s2buff.get()
        """


    import cProfile
    p = cProfile.Profile()
    p.enable()
    adv_test.test(module(), conf, verbose=0, mass=1)
    p.print_stats()
