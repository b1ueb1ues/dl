import adv_test
import adv

def module():
    return Curran

class Curran(adv.Adv):
    comment = "no fs"

    a1 = ('od',0.13)
    a3 = ('lo',0.5)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=2
        `s3
        """
    adv_test.test(module(), conf, verbose=-2)
