import adv_test
import adv
from adv import *
from module import energy

def module():
    return Lucretia

class Lucretia(adv.Adv):
    a3 = ('bk',0.3)
     
    def pre(this):
        if this.condition('energy'):
            this.init = this.c_init

    def init(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )
        this.conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel
            `s3 
            """
        Event('energized').listener(this.energy_doublebuff)

    def c_init(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'s2':2} ,
                team={'s1':1}
                )
        Event('energized').listener(this.energy_doublebuff)

    def energy_doublebuff(this, e):
        adv.Selfbuff("double_buff", 0.2, 15).on()



from slot.a import *
if __name__ == '__main__':

    conf = {}
    conf['slots.a'] = HH() + Jewels_of_the_Sun()

    if 1:
        conf['acl'] = """
            # e = this.energy.energized
            `s1, seq=5 and cancel and not e
            `s2, seq=5 and cancel and not e
            `s3, seq=5 and cancel and e or ( s=1 and e )
            """

    adv_test.test(module(), conf, verbose=0)



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
