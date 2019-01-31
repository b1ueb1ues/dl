import adv_test
from adv import *

def module():
    return Kuhai

class Kuhai(Adv):
    conf = {
        "mod_a"   : ('crit', 'damage', 0.15),
        } 
    def condition(this):
        this.conf["mod_a2"] = ('crit', 'damage', 0.15)
        return 'hp70'

    def init(this):
        this.s2fsbuff = Buff('s2ss',1,10,'ss','ss','self')

    def s2_proc(this, e):
        this.s2fsbuff.on() 

    def fs_proc(this, e):
        if this.s2fsbuff.get() > 0:
            this.dmg_make("o_s2fs",0)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

