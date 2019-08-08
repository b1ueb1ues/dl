if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *

def module():
    return Melsa

class Melsa(Adv):
    a3 = ('cc',0.08,'hit15')
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        C4FS C4FS C2- S1 C4FS C5- S2 C2- S1 C4FS C5- S3 C1- S1 C4FS C5-
        S2 C2- S1 C4FS C4FS C1- S1 C4FS C5- S3 C1- S2 C1- S1
    """



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

