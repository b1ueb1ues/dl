import adv_test
import adv

def module():
    return Amane

class Amane(adv.Adv):
    a3 = ('bk',0.2)
    a1 = ('prep','75%')



if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1
        `s2, seq=5 and cancel
        `s3
        """
    acl21 = """
        `s2
        `s1
        `s3, seq=5
        """ 
    # test that 21 is better than 12
    # s3 when c5missile come change some timeline to have a better dps
    if 0:
        conf['acl'] = acl21
        adv_test.test(module(), conf, verbose=0)

    conf['acl'] = acl12
    adv_test.test(module(), conf, verbose=0)


