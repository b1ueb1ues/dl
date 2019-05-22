import adv_test
from adv import *
from module.bleed import mBleed
import ieyasu 

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):

    def s2ifbleed(this):
        if this.s2buff.get()!=0:
            if this.bleed._static['stacks'] > 0:
                return 0.15
        return 0

    def init(this):
        this.s2buff = Selfbuff("s2",0.15, 15, 'crit')
        this.s2buff.modifier.get = this.s2ifbleed
        this.bleed = mBleed("g_bleed",0).reset()
        this.s2charge = 0

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.46).on()


if __name__ == '__main__':
    conf = {}

    if 1:
        conf['acl'] = """
            `s1, this.bleed._static['stacks'] < 3
            `s2, this.bleed._static['stacks'] > 0
            `s3
            """
    else:
        conf['acl'] = """
            `s1
            `s2, this.bleed._static['stacks'] > 0
            `s3
            """
    adv_test.test(module(), conf, verbose=0, mass=0)

