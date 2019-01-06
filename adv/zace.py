import adv_test
from adv import *

def module():
    return Zace

class Zace(Adv):
    comment = 'do not use fs'
    conf = {
        'mod_a':('s','passive',0.2),
    }


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

