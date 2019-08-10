if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Johanna

class Johanna(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

