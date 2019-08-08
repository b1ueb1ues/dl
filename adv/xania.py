if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv


def module():
    return Xania

class Xania(adv.Adv):
    a1 = ('s',0.20)
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {}
    #import slot
    #conf['slots.a'] = slot.a.Saintly_Delivery()+slot.a.RR()



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

