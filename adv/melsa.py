import adv_test
from adv import *

def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, cancel
        `s2, cancel
        `fs, x=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

