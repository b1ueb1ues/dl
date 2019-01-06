import adv_test
import adv

def module():
    return Hawk

class Hawk(adv.Adv):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)

