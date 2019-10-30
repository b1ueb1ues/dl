if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Malka

class Malka(Adv):
    comment = ''

    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['slot.a'] = RR()+BN()

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+JotS()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

