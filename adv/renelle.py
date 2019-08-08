if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.08,'hit15')
    conf['acl'] = """
        `rotation
        """
    conf['rotation_init'] = """
        c4fs C4FS C1- 
    """
    conf['rotation'] = """
        S1 C4FS C4FS C1- S1 C1- S2 C4FS C5- S1 C1- S3
        C4FS C5- S1 C2- S2 C4FS C5- S1 C4FS C4FS C1- S1 C1- S3 C1- S2 C4fs !c5!
    """
    # why c4fs at end, not c5

    def rinit(this):
        this.rotation('')

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

