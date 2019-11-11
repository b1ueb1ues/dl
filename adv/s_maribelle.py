if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
import slot
from slot.d import *

def module():
    return S_Maribelle

class S_Maribelle(adv.Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('bk',0.3)
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5 and cancel
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

