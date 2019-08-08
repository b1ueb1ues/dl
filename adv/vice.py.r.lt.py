if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Vice

class Vice(Adv):
    a1 = ('bk',0.2)
    #comment = 'reach 100 resist with Silke Lends a Hand'
    #import slot
    #conf = {}
    #conf['slots.a'] = slot.a.Silke_Lends_a_Hand()+slot.a.RR()




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
    """
    conf['rotation_init'] = """
        C4FS C4FS C1-
    """
    conf['rotation'] = """
        S1 C4FS C4FS C1- S1 C1- S2 C4FS C5- S1 C1- S3
        C4FS C5- S1 C2- S2 C4FS C5- S1 C4FS C4FS C1- S1 C1- S3 C1- S2 C5- c4fs
    """
    # why c4fs at last? why not c5?
    adv_test.test(module(), conf, verbose=0, mass=0)

