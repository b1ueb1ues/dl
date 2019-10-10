if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Waike


class Waike(adv.Adv):
    comment = 'no bog'
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """

    def d_slots(this):
        #this.conf.slot.d = DJ()
        return

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

