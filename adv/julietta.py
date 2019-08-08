if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Julietta

class Julietta(adv.Adv):
    comment = 'no fs & no s2'
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3,seq=4
        """
    adv_test.test(module(), conf, verbose=0)

