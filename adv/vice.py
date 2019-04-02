import adv_test
from adv import *

def module():
    return Vice

class Vice(Adv):
    comment = 'reach 100 resist with Silke Lends a Hand'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42

    conf = {
        "mod_a1": ('att', 'bp', 0.2*0.15)
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

