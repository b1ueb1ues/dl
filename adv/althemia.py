import adv_test
import adv

def module():
    return Althemia

class Althemia(adv.Adv):
    a1 = ('s',0.3,'hp100')

    conf = {}
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf)

