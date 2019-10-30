import adv_test
from adv import *
from slot.a import *

def module():
    return Malka

class Malka(Adv):
    comment = ''

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+JotS()
        else:
            this.conf.slot.a = RR()+BN()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

