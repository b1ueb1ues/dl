import adv_test
import adv
from module import energy

def module():
    return D_Xander

class D_Xander(adv.Adv):
    conf = {
        "mod_a3": ('sp', 'passive', 0.05) ,
        } 

    a = 0
    if a==1:
        conf["mod_wp"] = [('s','passive',0.25),
                         ('crit','chance',0.06,'hp70') ]
        conf["mod_wp2"] = [('fs','passive',0.40),
                           ('crit','damage',0.13) ]
    if a==2:
        conf["mod_wp"] = [('s','passive',0.25),
                         ('crit','chance',0.06,'hp70') ]
        conf["mod_wp2"] = [('crit','chance',0.09,'hit15'),
                           ('crit','damage',0.15) ]

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


