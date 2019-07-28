import adv_test
from adv import *
from adv import ieyasu
from module.bleed import mBleed
import slot

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    def prerun(this):
        this.s2buff = Selfbuff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = mBleed("g_bleed",0).reset()
        this.s2charge = 0

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=-2, mass=0)

    exit()
    def foo(this, e):
        return
    module().s1_proc = foo
    conf['acl'] = """
        `s1
        `s2, seq=5 and this.bleed._static['stacks'] > 0
        `s3
        """
    adv_test.test(module(), conf, verbose=1, mass=0)
