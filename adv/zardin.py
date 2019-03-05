import adv_test
import adv

def module():
    return Zardin

class Zardin(adv.Adv):
    conf = {
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } 
    def condition(this):
        this.conf['mod_a'] = ('att' , 'passive', 0.10)
        return 'hp100'


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

