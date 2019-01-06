import adv_test
from adv import *

def module():
    return Orsem

class Orsem(Adv):
    conf = {
        "mod_a"   : ('crit', 'chance', 0.10) ,
        "mod_a2"  : ('crit', 'chance', 0.06) ,
        'condition':'hp70, 15hits',

        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

