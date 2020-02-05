import adv.adv_test
from adv import *

def module():
    return Su_Fang

class Su_Fang(Adv):
    a3 = ('s',0.20)
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3
        `fs, seq=5
        """



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

