import adv_test
from adv import *

def module():
    return Vice

class Vice(Adv):
    conf = {
        "mod_a"   : ('att', 'bp', 0.2*0.15)
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

