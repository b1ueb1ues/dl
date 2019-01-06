import adv_test
import adv

def module():
    return Rodrigo

class Rodrigo(adv.Adv):
    conf = {
        "mod_a": ('att'  , 'passive' , 0.08) ,
        'condition':'hp70',
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

