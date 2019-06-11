import adv_test
import naveed
import adv
from slot.a import *

def module():
    return Naveed

class Naveed(naveed.Naveed):
    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level > 5:
            this.s1level = 5
        adv.Event('defchain')()
    


if __name__ == '__main__':
    conf = {}
#    Naveed.comment = 'VC + RR'
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    conf['slots.a'] = VC()+RR()
    #conf['slots.a'] = VC()+Evening_of_Luxury()
    adv_test.test(module(), conf, verbose=0)



