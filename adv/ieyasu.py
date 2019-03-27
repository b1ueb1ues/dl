import adv_test
from adv import *
from module.bleed import Bleed

def module():
    return Ieyasu

class Ieyasu(Adv):
    conf = {
        "mod_a1": ('crit', 'chance', 0.1, 'hp70') ,
        "mod_a3": ('crit', 'damage', 0.2) ,
        } 


    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static['stacks'] > 0:
                return 0.15
        return 0


    def init(this):
        random.seed()
        this.s2buff = Selfbuff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Bleed("g_bleed",0).reset()
 #       this.crit_mod = this.rand_crit_mod
        this.s2charge = 0

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.46).on()


    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=1, mass=1)

    exit()
    def foo(this, e):
        return
    module().s1_proc = foo
    conf['acl'] = """
        `s1
        `s2, this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=1, mass=1)
