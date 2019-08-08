if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv

def module():
    return Rawn

class Rawn(adv.Adv):
    conf = {}
    conf['acl'] = """
    `s1, seq=5 or fsc
    `s2, seq=5 or fsc
    `s3, seq=5 or fsc
    """

    def prerun(this):
        if this.condition('c1+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=1
                """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)
