import adv_test
from adv import *

def module():
    return Berserker

class Berserker(Adv):
    def condition(this):
        this.init = this.c_init
        return 'last offense'

    def c_init(this):
        Buff('last_offense',0.4,15,wide='self').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

