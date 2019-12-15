import adv_test
import adv
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Luca

class Luca(adv.Adv):
    a1 = ('a',0.13,'hp100')

    conf = {}
    conf['slot.a'] = SotS()+Dear_Diary()
    conf['slot.d'] = C_Phoenix()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.paralysis.resist=0
        else:
            this.afflics.paralysis.resist=100

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s1_proc(this, e):
        this.afflics.paralysis('s1',110,0.883)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
