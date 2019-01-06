import adv_test
import adv

def module():
    return Melody

class Melody(adv.Adv):
    conf = {
        "mod_p"   : ('crit'  , 'chance', 0.08) ,
        'condition':'hp100',
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

