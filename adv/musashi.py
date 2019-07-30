import adv_test
import adv
from slot.d import *

def module():
    return Musashi

class Musashi(adv.Adv):
    a1 = ('lo',0.40)
    a3 = ('od',0.08)

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.resist['poison'] = 0
            #this.afflics.luck = 100

    def s1_proc(this, e):
        this.afflics.add('s1','poison',110,15,0.53,2.99)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 
        `s1
        `s3, s
        """
    #conf['slot.d'] = Pazuzu()
    adv_test.test(module(), conf, verbose=0, mass=10)

