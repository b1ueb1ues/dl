if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Ryozen

class Ryozen(Adv):
    a3 = ('od',0.08)
    conf = {}
    conf['acl'] = """
        `s2
        `s3
        `fs, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

