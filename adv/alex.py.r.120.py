import adv.adv_test
import adv
from slot.d import *

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
    """
    conf['rotation'] = """
        C4FS C5- S1 C4FS C5- S1 C1- S2 C4FS C5- S1 C5- S3 C5- S1
        C5- S2 C5- S1 C4FS C5- S1 C4- S3 C4- S2 C3- S1
    """
    adv_test.test(module(), conf, verbose=0)


