import adv_test
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
        c4fs c4fs s1
        c4fs c4fs s1
        c3 s2
        c4fs c4fs s1
        c1 s3
        """
    adv_test.test(module(), conf, verbose=0)


