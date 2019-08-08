if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Jakob

class Jakob(adv.Adv):
    comment = 'no bog'

    def d_slots(this):
        this.conf.slot.d = DJ()
        return

    def prerun(this):
        this.charge_p('prep','50%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

