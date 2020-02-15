import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Sylas

class Sylas(Adv):
    a3 = ('a',0.13,'hp70')

    comment = 'not consider skill haste for team'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    conf['slot.d'] = Vayu()
    conf['slot.a'] = RR()+The_Fires_of_Hate()
    conf['afflict_res.poison'] = 0

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        adv.Selfbuff('s2_shaste',0.20,15,'sp','buff').on()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

