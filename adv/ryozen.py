import adv_test
from adv import *

def module():
    return Ryozen

class Ryozen(Adv):
    a3 = ('od',0.08)


    def debug(this):
        print this.all_modifiers

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

