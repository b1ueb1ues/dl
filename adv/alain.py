import adv_test
from adv import *

def module():
    return Alain

class Alain(Adv):
    conf = {}
    comment = 'reach 100 resist with Saintly Delivery'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

