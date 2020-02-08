import adv.adv_test
import adv

def module():
    return Malora

class Malora(adv.Adv):
    a1 = ('bk',0.2)
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
