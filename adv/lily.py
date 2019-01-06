import adv_test
import adv

def module():
    return Lily

class Lily(adv.Adv):
    conf = {
        "mod_a"  : ('att'  , 'passive' , 0.15)  ,
        "mod_d"  :[('att'  , 'passive' , 0.45)  ,
                   ('crit' , 'chance'  , 0.20)] ,
        'condition':'hp100',
        } 
    def init(this):
        this.charge("prep", "100%")


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        #prep=0
        #if pin=='prep': prep=1
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s1, pin='prep'
        """

    adv_test.test(module(), conf, verbose=0)



