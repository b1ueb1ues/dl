import adv_test
from adv import *

def module():
    return Orsem

class Orsem(Adv):
    conf = {
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } 

    def pre(this):
        if this.condition('hit15'):
            this.conf['mod_a'] = ('crit' , 'passive', 0.10)
        if this.condition('hp70'):
            this.conf['mod_a2'] = ('crit' , 'passive', 0.06)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

