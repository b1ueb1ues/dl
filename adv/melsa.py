import adv.adv_test
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
        C4FS C4FS C2- S1 C4FS C5- S2 C2- S1 C4FS C5- S3 C1- S1 C4FS C5-
        S2 C2- S1 C4FS C4FS C1- S1 C4FS C5- S3 C1- S2 C1- S1
    """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

