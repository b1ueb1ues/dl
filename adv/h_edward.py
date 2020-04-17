import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Halloween_Edward

class Halloween_Edward(Adv):
    a1 = ('a',0.1,'hp100')

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Seaside_Princess()
    conf['acl'] = """
        `s1
        `s2, seq=5 
        `s3, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

