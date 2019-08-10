if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Zardin

class Zardin(adv.Adv):
#    comment = 'Stellar_Show+RR'
    a1 = ('a',0.10,'hp100')
    conf = {}
    #conf['slot.d'] = DJ
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """

    a = 2
    if a==1:
        conf["slots.a"] = RR() + Stellar_Show()
    if a==2:
        conf["slots.a"] = TSO() + LC()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

