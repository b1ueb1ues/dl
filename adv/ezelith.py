import adv_test
from adv import *

def module():
    return Ezelith

class Ezelith(Adv):
    conf = {
        "mod_a": ('att', 'broken_p', 0.3*0.15) ,
        } 

    def init(this):
        random.seed()
        this.s2buff = Buff("s2",0.15, 15,'att','buff','self')

    def s2_proc(this, e):
        this.s2buff.on()

    def dmg_proc(this, name, amount):
        if name[0] != 'x':
            return
        if this.s2buff.get():
            r = random.random()
            if r < 0.5:
                Buff("s2_ab",-0.05,5,'def').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """

    adv_test.test(module(), conf, mass=1)

