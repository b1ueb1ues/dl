import adv_test
import adv
from slot.a import *

def module():
    return Lily

class Lily(adv.Adv):
    comment = '(RR+EoL>RR+LC>RR+CE at hp100'
    comment += ';RR+LC=RR+CE at hp70)'
    conf = {}
    conf['slot.a'] = RR()+LC()
    a1 = ('a',0.15,'hp100')
    a3 = ('prep','100%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        #prep=0
        #if pin=='prep': prep=1
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s2, pin='prep'
        """

    adv_test.test(module(), conf, verbose=0)



