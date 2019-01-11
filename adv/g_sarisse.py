import adv_test
import adv
from adv import *

def module():
    return G_Sarisse

class G_Sarisse(adv.Adv):
    def init(this):
        this.hits = 0
        this.buffs = adv.Buff()
        this.s2stance = 0

    def dmg_proc(this, name, amount):
        if name[:2] == 'x1':
            this.hits += 3
        elif name[:2] == 'x2':
            this.hits += 2
        elif name[:2] == 'x3':
            this.hits += 3
        elif name[:2] == 'x4':
            this.hits += 2
        elif name[:2] == 'x5':
            this.hits += 5
        elif name[:2] == 'fs':
            this.hits += 8
        if this.hits >= 20:
            this.hits -= 20
            adv.Buff('sylvan strength',0.02,15*1.3,wide='self').on()
            adv.Buff('sylvan crit',0.01,15*1.3,'crit','chance',wide='self').on()

    def s1_proc(this, e):
        buffcount = 0
        for i in this.buffs._static.all_buffs:
            if buffcount >= 7:
                break
            if i.get():
                buffcount += 1
        this.dmg_make('s1_missile*%d'%buffcount,0.77*buffcount)
        this.hits += 1 + buffcount
            

    def s2_proc(this, e):
        if this.s2stance == 0:
            adv.Buff('s2str',0.20,13).on()
            this.s2stance = 1
        elif this.s2stance ==0:
            log('buff','def')
            this.s2stance = 0


if __name__ == '__main__':
    module().comment = 'c4+fs'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=4
        """

    adv_test.test(module(), conf, verbose=0)

    module().comment = 'c1+fs'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)

