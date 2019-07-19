import adv_test
from adv import *

def module():
    return Irfan

class Irfan(Adv):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
    """
    conf['rotation_init'] = """
        c4fs c4fs c1
    """
    conf['rotation'] = """
        S1 C4FS C4FS C1- S1 C2- S2 C4FS C5- S3 C3- S1 C4FS
        C5- S2 C1- S1 C4FS C4FS C1- S1 C4FS C4- S3 C3- S1 C1- S2 C4FS C5-
    """
    adv_test.test(module(), conf, verbose=0, mass=0)

