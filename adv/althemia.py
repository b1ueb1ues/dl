if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Althemia

class Althemia(adv.Adv):
    a1 = ('s',0.3,'hp100')
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3
        `s2, s=1
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf)

