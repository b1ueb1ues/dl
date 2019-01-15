import adv_test
from adv import *
from module import energy

def module():
    return Annelie

class Annelie(Adv):
    comment = 'unconfirmed frame data'
    conf = {
        "mod_a"  : ('s', 'passive', 0.35) ,
        'condition':'hp70',
        's1_recovery':2.5,
        's2_recovery':3.55,
        } 

    def init(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={'1':1,'2':2},
                team={'s2':2}
                )
        Event('energized').listener(this.energy_doublebuff)

    def energy_doublebuff(this, e):
        Buff("double_buff", 0.2, 15,'att',wide='self').on()

    def s1_proc(this, e):
        if this.stance == 0:
            this.dmg_make('s1_p1',0.1+8.14)
            this.energy.add_energy('1')
            this.stance = 1
        elif this.stance == 1:
            this.dmg_make('s1_p2',2*(0.1+4.07))
            this.energy.add_energy('2')
            this.stance = 2
        elif this.stance == 2:
            this.dmg_make('s1_p3',3*(0.1+3.54))
            this.stance = 0



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

