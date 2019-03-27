import adv_test
import adv
from module import energy

def module():
    return D_Xander

class D_Xander(adv.Adv):
    conf = {
        "mod_a3": ('sp', 'passive', 0.05) ,
        } 

    def pre(this):
        if this.condition('energy'):
            this.init = this.c_init

    def init(this):
        energy.Energy(this,
                self={},
                team={}
                )

    def c_init(this):
        energy.Energy(this,
                self={'s2':1},
                team={'s2':1}
                )


if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel or s
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    conf['acl'] = acl12
    adv_test.test(module(), conf, verbose=0)


