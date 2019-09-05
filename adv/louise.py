if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Louise

class Louise(adv.Adv):
    a1 = ('od',0.13)
    comment = 'no fs'
    conf = {}
    conf['slot.d'] = Pazuzu()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100


    def s1_proc(this, e):
        this.afflics.poison('s1', 120, 0.582)


    def s2_proc(this, e):
        coef = (4.035-2.69)*3 * this.afflics.poison.get()
        this.dmg_make("o_s2_boost", coef)


if __name__ == '__main__':
    conf = {}
<<<<<<< HEAD
=======
    from slot.d import *
#    conf['slot.d'] = Pazuzu()
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
>>>>>>> 6b78f8fa15998993caa80b6c544dd8cbfe1a11b9
    adv_test.test(module(), conf, verbose=0)
