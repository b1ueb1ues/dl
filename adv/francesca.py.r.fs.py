import adv_test
from adv import *
from slot.a import *

def module():
    return Francesca

class Francesca(Adv):
    a1 = ('fs',0.30)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['slot.a'] = RR()+SS()
    conf['rotation'] = """
        C2FSC2FSC2FS C2FS- S1 
        C2FSC2FSC2FS C2FS- S1 C2FS- S2 
        C2FSC2FS C2FS- S1 C2FS- S3
        C2FSC2FS C2FS- S1
        C2FS C2FS- S2 C2FS C2FS- S1 
        C2FSC2FSC2FS C2FS- S1 C2FS C2FS- S3 C2FS- S2 C2FS- S1
    """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

