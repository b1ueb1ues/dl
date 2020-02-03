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
        `s3, not this.s3_buff_on
        `s1
        `s2
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

