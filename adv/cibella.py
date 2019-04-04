import adv_test
from adv import *

def module():
    return Cibella

class Cibella(Adv):
    conf = {}
    comment = 'reach 100 resist with Saintly Delivery'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

