import adv_test
import adv

def module():
    return Aoi

class Aoi(adv.Adv):
    conf = {
        "mod_a1": ('att', 'punisher', 0.08*0.45),
        } 
    

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

