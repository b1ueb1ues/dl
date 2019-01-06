import adv_test
import adv

def module():
    return Aoi

class Aoi(adv.Adv):
    conf = {
        "mod_a": ('att', 'punisher', 0.04),
        } 
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

