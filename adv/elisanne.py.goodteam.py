import adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = '10000 team dps; no s2'
    a1 = ('bt',0.25)

    conf = {}
    #conf['slots.a'] = CE() + Bellathorna()
    #conf['slots.a'] = Halidom_Grooms() + Bellathorna()
    #conf['slots.a'] = HG() + Indelible_Summer()
    conf['slots.a'] = BB() + JotS()
    conf['slots.d'] = DJ()
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf['acl'] = """
                        `s1
                        """
        else:
            this.conf['acl'] = """
                        `s1
                        `s2, fsc
                        `fs, seq=5
                        """


if __name__ == '__main__':
    conf = {}
    #conf['acl'] = """
    #    `s1, seq=5 and cancel
    #    `s2, seq=5 and cancel
    #    `s3, seq=5 and cancel
    #    """
    # conf['acl'] = """
    #     `s1
    #     `fs, seq=5
    #     """


    adv_test.team_dps = 10000
    adv_test.test(module(), conf, verbose=-2)
