import adv_test
from adv import *

def module():
    return Orion

class Orion(Adv):
    conf = {
        "mod_a": ('crit', 'chance', 0.10),
        'condition':'15hits',
        } 

    def init(this):
        this.charge('prep','50%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

