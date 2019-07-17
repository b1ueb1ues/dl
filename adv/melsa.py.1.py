import adv_test
from adv import *

def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        4C+FS+4C+FS+1C s1
        4C+FS+4C+FS+1C s1 s2
        4C+FS+4C+FS+1C s1
        c1 s3
    """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

