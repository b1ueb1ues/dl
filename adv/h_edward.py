if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return H_Edward

class H_Edward(adv.Adv):
    a1 = ('a',0.1,'hp100')

    conf = {}
    conf['slot.a'] = Resounding_Rendition()+Seaside_Princess()
    conf['acl'] = """
        `s1
        `s2, seq=5 
        `s3, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

