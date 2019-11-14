if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Chelsea

class Chelsea(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """

    def prerun(this):
        this.hp = 100
        this.obsession = 0
        
        this.a1atk = Selfbuff('a1atk',0.20,-1,'att','passive')
        this.a1spd = Spdbuff('a1spd',0.10,-1)
        this.a3 = Selfbuff('a3_str_passive',0.3,60,'att','passive')

    def dmg_before(this, name):
        hpold = this.hp
        
        if name != 's1' and this.a3.get():
            this.hp -= 3 * this.obsession

        if this.hp <= 0:
            this.hp = hpold
        elif this.hp > 100:
            this.hp = 100

        if this.hp <= 30:
            this.a1atk.on()
            this.a1spd.on()
        else:
            this.a1atk.off()
            this.a1spd.off()

    def dmg_proc(this, name, amount):
        hpold = this.hp
        
        if name == 's1' and this.a3.get():
            this.hp += 7

        if this.hp <= 0:
            this.hp = hpold
        elif this.hp > 100:
            this.hp = 100

        if this.hp <= 30:
            this.a1atk.on()
            this.a1spd.on()
        else:
            this.a1atk.off()
            this.a1spd.off()

    def s1_proc(this, e):
        hpold = this.hp
        
        if this.a3.get():
            this.hp -= 3 * this.obsession

        if this.hp <= 0:
            this.hp = hpold
        elif this.hp > 100:
            this.hp = 100

        if this.hp <= 30:
            this.a1atk.on()
            this.a1spd.on()
        else:
            this.a1atk.off()
            this.a1spd.off()
        
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)
        this.dmg_make('s1',1.36)

    def s2_proc(this, e):
        Selfbuff('s2',0.3,60).on()
        this.obsession = Selfbuff('s2').stack()
        this.a3.on()

    def dmg_make(this, name, dmg_coef, dtype=None):
        if dtype == None:
            dtype = name
        this.dmg_before(name)
        count = this.dmg_formula(dtype, dmg_coef)
        log('dmg', name, count)
        this.dmg_proc(name, count)
        return count

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)
