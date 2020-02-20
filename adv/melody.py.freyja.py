import adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(Adv):
    comment = 'no s2; Freyja'
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = HG()+FWHC()
    conf['slots.d'] = Freyja()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        """
    
    adv.adv_test.test(module(), conf)

