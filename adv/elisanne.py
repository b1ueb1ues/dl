import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = 'no s2 or s3'
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.a'] = BB() + FWHC()
    conf['slots.d'] = H_Maritimus()
    conf['acl'] = """
        `s1
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
