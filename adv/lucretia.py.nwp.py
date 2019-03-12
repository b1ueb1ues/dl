import adv_test
import adv
from adv import *
from module import energy

def module():
    return Lucretia

class Lucretia(adv.Adv):
    prep = 0
    lastoffence = 0

    def condition(this):
        this.init = this.c_init
        return 'energy'

    def init(this):
        energy.Energy(this,
                self={} ,
                team={} 
                )
        Event('energized').listener(this.energy_doublebuff)

    def c_init(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'s2':2,'prep':5} ,
                team={'s1':1,'s2':2} 
                )
        Event('energized').listener(this.energy_doublebuff)
        if this.prep:
            this.energy.add_energy(this.prep)
        if this.lastoffence:
            adv.Buff('lo',0.4,15).on()


    def energy_doublebuff(this, e):
        adv.Buff("double_buff", 0.2, 15,'att',wide='self').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, sx=2 
        `s1, sx=3
        `s1, seq=5 and cancel
        """

    if 1:
        conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel
            `s3, seq=5 and cancel
            """

    #adv_test.test(module(), conf, verbose=0)

    conf['mod_wp'] = ('s','passive',0.25)
    #adv_test.test(module(), conf, verbose=0)

    conf['mod_wp'] = []
    module().prep = 'prep'
    adv_test.test(module(), conf, verbose=0)
    module().prep = 0

    module().lastoffence = 1
    adv_test.test(module(), conf, verbose=0)
    module().prep = 0



'''
2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 5 0.| 2 2 3 | 5 0 | 2 2 3 |

2 1 | 2 1 3 | 2 1 | 2 1 3 | 
2 3 | 5 0 0 | 2 3 | 5 0 0 |

2 1 | 2 3 1 | 2 1 | 2 3 1 | 
2 3 | 5 0 1 | 3 4 | 6.0 1 |

2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 1 2 | 3 2 1
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 4 6.| 0 2 3
'''
