if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Lathna

class Lathna(Adv):
    conf = {}
    conf['slot.a'] = RR()+JotS()
    conf['acl'] = """
        # s1a = this.s1a
        `s1a
        `s2
        `s3, seq=5
        """
    conf['cond_afflict_res'] = 0
    def prerun(this):
        this.s1tmp = Conf(this.conf.s1)
        if this.condition('{} resist with poisoner in team'.format(this.conf['cond_afflict_res'])):
            this.enable_s1_boost = True
            this.afflics.poison.resist = this.conf['cond_afflict_res']
        else:
            this.enable_s1_boost = False
            this.afflics.poison.resist = 100

    def s1back(this, t):
        this.conf.s1.recovery = this.s1tmp.recovery
        this.conf.s1.dmg = this.s1tmp.dmg

    def s1a(this):
        if this.s1.check():
            this.conf.s1.dmg += 1.58*4
            if this.enable_s1_boost:
                coef = (3.555-1.58)*7
                this.dmg_make("o_s1_boost", coef)
            this.conf.s1.recovery = 4.07
            Timer(this.s1back).on(this.conf.s1.startup+0.01)
            return this.s1()
        else:
            return 0

if __name__ == '__main__':
    adv_test.test(module(), conf, verbose=0)

