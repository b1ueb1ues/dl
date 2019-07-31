import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
#    comment = 'RR+Bellathorna'
    a1 = ('bt',0.25)

    conf = {}
    #conf['slots.a'] = RR() + HG()
    #conf['slots.a'] = Halidom_Grooms() + Bellathorna()
    conf['slots.a'] = HG() + Indelible_Summer()
    conf['slots.d'] = DJ()
    #conf['mod'] = {'ex':('sp','passive',0.15)}


if __name__ == '__main__':
    conf = {}
    #conf['acl'] = """
    #    `s1, seq=5 and cancel
    #    `s2, seq=5 and cancel
    #    `s3, seq=5 and cancel
    #    """
    conf['acl'] = """
        `s1
        `s2, fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)
