import adv_test
import adv

def module():
    return Louise

class Louise(adv.Adv):
    conf = {
        "mod_a_od" : ('att' , 'punisher' , 0.13*0.45) ,
        } 

    def init(this):
        pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    adv_test.test(module(), conf, verbose=0)

