import adv_test
import adv

def module():
    return Althemia

class Althemia(adv.Adv):
    a1 = ('s',0.3,'hp100')


if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3
        `s2, s=1
        """
    adv_test.test(module(), conf)

