if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
#    comment = 'RR+Bellathorna'
    a1 = ('bt',0.25)

    conf = {}
    #conf['slots.a'] = RR() + HG()
    #conf['slots.a'] = Halidom_Grooms() + Bellathorna()
    #conf['slots.a'] = HG() + Indelible_Summer()
    conf['slots.a'] = BB() + JotS()
    conf['slots.d'] = DJ()
    #conf['mod'] = {'ex':('sp','passive',0.15)}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf['acl'] = """
                        `s1
                        `s2, seq=5
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
    #     `s2, fsc
    #     `fs, seq=5
    #     """

#    conf['acl'] = '''
#        `rotation
#    '''
#    conf['rotation'] = """
#        c5c5fss1
#    """
#    conf['rotation'] = """
#        c5fsc5s1
#    """
    adv_test.test(module(), conf, verbose=-2)
