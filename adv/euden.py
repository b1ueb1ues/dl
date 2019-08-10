if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv


def module():
    return Euden

class Euden(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

