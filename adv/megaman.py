import adv_test
from adv import *
from module.bleed import Bleed

def module():
    return Megaman

class Megaman(Adv):

    def prerun(this):
        this.ammo = {
                '1':2000,
                '2':4000,
                }

        this.bleed = Bleed("g_bleed",0).reset()

    def dmg_proc(this, name, amount):
        print(this.ammo['1'])
        print(this.ammo['2'])
        if name == 'x1_missile':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x2_missile':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x3_missile':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x4_missile':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'x5_missile':
            this.ammo['1'] += 50
            this.ammo['2'] += 50
        elif name == 'fs':
            this.ammo['1'] += 180
            this.ammo['2'] += 180

    def s1_proc(this, e):

    def s2_proc(this, e):

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        # bs = this.bleed._static['stacks']
        `s1, bs <= 1 and this.ammo['1'] >= 1000
        `s2, this.ammo['2'] >= 1000
        `s3, seq=5
    """

    adv_test.test(module(), conf, verbose=0)
