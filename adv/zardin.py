import adv_test
import adv

def module():
    return Zardin

class Zardin(adv.Adv):
    conf = {
        "mod_a"   : ('att'  , 'passive' , 0.10)  ,
        'condition':'hp100',
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

