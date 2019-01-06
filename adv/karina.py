import adv_test
import adv

def module():
    return Karina

class Karina(adv.Adv):
    conf = {
        "mod_d" :[('att'  , 'passive' , 0.45)  ,
                  ('crit' , 'chance'  , 0.20)] ,
        } 

    def init(this):
        this.charge("prep","50%")



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

