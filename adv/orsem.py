if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Orsem

class Orsem(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        C4FS C4FS C2- S1 C4FS C5- S2 C1- S1 C4FS C5- S3 C1- S1 C4FS C5-
        S2 C1- S1 C4FS C4FS C1- S1 C4FS C5- S3 C1- S2 C1- S1
    """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

