if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Joe

class Joe(adv.Adv):
    conf = {}
    #conf['slots.a'] = RR()+EE()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.burn.resist=0
        else:
            this.afflics.burn.resist=100
        if this.condition('fullhp=burn'):
            this.fullhp = 1
        else:
            this.fullhp = 0

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s2_proc(this, e):
        this.afflics.burn('s2',90+40*this.fullhp,0.6)




if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

