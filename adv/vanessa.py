if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)
    conf = {}
    conf['slot.a'] = KFM()+CE()
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=4
        `fs,seq=5
        """



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

