import adv_test
from adv import *

def module():
    return Berserker

class Berserker(Adv):
    def init(this):
        if this.condition('last offense'):
            Buff('last_offense',0.4,15,wide='self').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

