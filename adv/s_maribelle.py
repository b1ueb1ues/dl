import adv_test
import adv
import slot
from slot.d import *

def module():
    return S_Maribelle

class S_Maribelle(adv.Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('bk',0.3)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5 and cancel
        """

    #conf['slots.d'] = Cerberus()
    #from slot.w import *
    #conf['slots.w'] = wand5b2p2()
    #conf['acl'] = """
    #    `s1, seq=5 and cancel
    #    `s2, seq=5 and cancel
    #    `s3, seq=5
    #    """
    adv_test.test(module(), conf, verbose=0)

