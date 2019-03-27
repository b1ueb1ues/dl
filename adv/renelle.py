import adv_test
from adv import *

def module():
    return Renelle

class Renelle(Adv):
    def pre(this):
        if this.condition('hit15'):
            this.conf['mod_a'] = ('crit' , 'passive', 0.08)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

