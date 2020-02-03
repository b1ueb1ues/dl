import adv.adv_test
import adv
from slot.d import *

def module():
    return Pietro

class Pietro(adv.Adv):
    a1 = ('cd',0.13)
#    comment = 'unsuitable resist'
    conf = {}
    conf['acl'] = """
        `s1
        `s3,seq=4
        `fs,seq=5
        """

    def d_slots(this):
        this.conf.slots.d = Siren()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

