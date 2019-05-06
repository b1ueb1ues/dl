import adv_test
from adv import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

