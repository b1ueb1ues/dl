import adv_test
from adv import *
import mikoto

def module():
    return Mikoto

class Mikoto(mikoto.Mikoto):
    conf = {
        "mod_a2"  : ('crit' , 'chance'  , 0.08) ,
        }
    conf['str_w'] = 1.5*353
    conf['mod_w'] = ('att','punisher',0.2)

    def init(this):
        mikoto.Mikoto.init(this)
        this.charge_p('prep','50%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)

