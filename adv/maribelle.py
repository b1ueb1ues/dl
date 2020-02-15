import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Maribelle

class Maribelle(Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('prep','100%')
    conf = {}
    conf['slots.d'] = Garland()
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

