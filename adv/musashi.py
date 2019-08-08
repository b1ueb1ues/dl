if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Musashi

class Musashi(adv.Adv):
    a1 = ('lo',0.40)
    a3 = ('od',0.08)
    conf = {}
    conf['acl'] = """
        `s2, seq=5 
        `s1
        `s3, s
        """
    conf['slot.d'] = Pazuzu()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
            #this.afflics.poison.tolerance = 5
        else:
            this.afflics.poison.resist=100

    def s1_proc(this, e):
        this.afflics.poison('s1',110,0.53)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

