if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv
from slot.a import *

def module():
    return Sylas

class Sylas(adv.Adv):
    a3 = ('a',0.13,'hp70')

    comment = 'not consider skill haste for team'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=5
        """

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

    def s1_proc(this, e):
        this.afflics.poison('s1',120,0.582)

    def s2_proc(this, e):
        adv.Selfbuff('s2_shaste',0.20,15,'sp','buff').on()



if __name__ == '__main__':
    adv_test.test(module(), conf, verbose=0)

