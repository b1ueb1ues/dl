import adv.adv_test
import adv.ezelith
from adv import Debuff

def module():
    return Ezelith

class Ezelith(adv.ezelith.Ezelith):

    def dmg_proc(this, name, amount):    
        if name[0] != 'x':
            return
        if this.s2buff.get():
            # r = random.random()
            # if r < this.s2chance:
            #     Debuff("s2_ab",0.05,5,1).on()
            Debuff('s2_ab', 0.05, 5, this.s2chance).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, mass=0, verbose=-2)

