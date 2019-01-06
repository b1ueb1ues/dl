import adv_test
from adv import *

def module():
    return Ryozen

class Ryozen(Adv):
    conf = {
        'mod_a':('att','op',0.08*0.45),
        }


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

