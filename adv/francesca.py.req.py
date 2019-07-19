import adv_test
from adv import *

def module():
    return Francesca

class Francesca(Adv):
    a1 = ('fs',0.30)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        C4FS C4FS C1- S1 C4FS C4FS C1- S1 C1- S2 C4FS C5- S1 C1- S3
    """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

