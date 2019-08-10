if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Alain

class Alain(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    #comment = 'reach 100 resist with Saintly Delivery'
    #conf = {
    #        'slots.a': RR()+Saintly_Delivery()
    #    }


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

