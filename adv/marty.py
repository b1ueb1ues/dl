if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv

def module():
    return Marty

class Marty(adv.Adv):
    a1 = ('sp',0.05)
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {}
    #import slot
    #conf['slots.a'] = slot.a.Saintly_Delivery()+slot.a.RR()
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s3,fsc
        `fs, seq=3
        """



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

