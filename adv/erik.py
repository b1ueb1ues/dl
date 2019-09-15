import adv_test
import adv
from slot.a import *

def module():
    return Erik

class Erik(adv.Adv):
    comment =''
    a1 = ('fs',0.30)
    import slot.a
    conf = {}
    conf['slot.a'] = slot.a.KFM()+slot.a.CE()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,fsc
        `s3,fsc
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

