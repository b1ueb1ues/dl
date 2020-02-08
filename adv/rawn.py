import adv.adv_test
import adv

def module():
    return Rawn

class Rawn(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1, cancel
        `s2, cancel
        `s3, cancel
        `fs, x=4
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
