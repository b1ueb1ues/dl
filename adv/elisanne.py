import adv_test
from adv import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = 'do not use fs & RR+15%buff_time'
    conf = {}
    conf['mod_a'] = ('buff','time',0.25)
    conf['mod_wp2'] = ('buff','time',0.15)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=-2)


