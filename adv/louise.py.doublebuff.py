import adv_test
import adv
from slot.a import *
import louise

def module():
    return Louise

class Louise(louise.Louise):

    def init(this):
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        adv.Buff('double',(0.13+0.08)*7,30).on()



if __name__ == '__main__':
    module().comment = 'poison 3 times & no fs & g_ranzal+lowen'
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    conf['slots.a'] = RR()+VC()
    adv_test.test(module(), conf, verbose=0)
