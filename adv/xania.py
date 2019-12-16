import adv_test
import adv


def module():
    return Xania

class Xania(adv.Adv):
    a1 = ('s',0.20)
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {}
    #import slot
    #conf['slots.a'] = slot.a.Saintly_Delivery()+slot.a.RR()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

