if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return H_Edward

class H_Edward(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 
        `s3, seq=5
        """
    a1 = ('a',0.1,'hp100')


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

