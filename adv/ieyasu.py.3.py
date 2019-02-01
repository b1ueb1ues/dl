import adv_test
from adv import *
from module.bleed import Bleed
import ieyasu 

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    class Bleed(Bleed):
        def dot_end_proc(this, e):
            return

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static.stacks > 0:
                return 0.15
        return 0

    def init(this):
        this.s2buff = Buff("s2",0.15, 15, 'crit', wide='self')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = Ieyasu.Bleed("g_bleed",0).reset()
        this.s2charge = 0

    def s1_proc(this, e):
        Ieyasu.Bleed("s1_bleed", 1.46).on()
        Ieyasu.Bleed("s1_bleed", 1.46).on()
        Ieyasu.Bleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

