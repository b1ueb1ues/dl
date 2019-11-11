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
    conf = {}
    conf['acl'] = """
        `s1
        `s3,fsc
        `fs,seq=5
        """
    conf['slot.d'] = DJ()

    def prerun(this):
        this.charge_p('prep','50%')


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

