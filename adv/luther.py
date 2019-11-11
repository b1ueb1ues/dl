if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Luther

class Luther(Adv):
    a1 = ('cc',0.10,'hit15')
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

