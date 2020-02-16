import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Joe

class Joe(Adv):
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = Mega_Friends()+Dear_Diary()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, x=3
        """
    conf['afflict_res.burn'] = 0

    def prerun(this):
        if this.condition('hp100'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        this.afflics.burn('s1',100+70*this.fullhp,0.803)
        
    def s2_proc(this, e):
        this.afflics.burn('s2',100+70*this.fullhp,0.803)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

