import adv.adv_test
import adv
from slot.a import *

def module():
    return Julietta

class Julietta(adv.Adv):
    comment = 'do not use fs'
    conf = {}
    conf['slots.a'] = KFM()+VC()

    def s2_proc(this, e):
       adv.Event('defchain')()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,seq=5
        `s3,seq=4
        """
    adv_test.test(module(), conf, verbose=0)

