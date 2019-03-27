import adv_test
from adv import *
import copy
from module.fsalt import *
import albert


def module():
    return Albert


class Albert(albert.Albert):
    conf = {
            'mod_a1':('fs','passive',0.5),
            'mod_wp2':[],
            }

    def init(this):
        this.charge_p('prep','100%')
        albert.Albert.init(this)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1, this.s2.charged > 900
        `s3
        `fs, seq=2
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

