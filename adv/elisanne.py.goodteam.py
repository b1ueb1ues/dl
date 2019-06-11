import adv_test
from adv import *
from slot.a import *


def module():
    return Elisanne

class Elisanne(Adv):
    comment = '5000 team dps; no s2'
    a1 = ('bt',0.25)

    conf = {
            'slots.a': CE() + Bellathorna()
            }



if __name__ == '__main__':
    conf = {}
    #conf['acl'] = """
    #    `s1, seq=5 and cancel
    #    `s2, seq=5 and cancel
    #    `s3, seq=5 and cancel
    #    """
    conf['acl'] = """
        `s1
        `fs, seq=5
        """
    adv_test.team_dps = 2500+2000+500
    adv_test.test(module(), conf, verbose=-2)


