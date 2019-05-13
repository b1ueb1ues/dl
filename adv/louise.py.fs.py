import adv_test
import adv

def module():
    return Louise

class Louise(adv.Adv):
    a1 = ('od',0.13)
    def pre(this):
        this.conf.mod = {'ex':('sp','passive',0.15)}
        this.conf.dodge.recovery = 20.0/60
        this.conf.dodge.startup = 23.0/60


    def init(this):
        this.a_dodge.cancel_by = ['fs']
        adv.Listener('dodge',this.l_dodge)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)

    def l_dodge(this, e):
        this.think_pin('dodge')



if __name__ == '__main__':
    module().comment = 'poison 3 times & fs dodge & SS+Bonds & with own co-a'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs
        `dodge, fsc
        """
    from slot.a import *
    conf['slots.a'] = Stellar_Show() + Forest_Bonds()
    adv_test.test(module(), conf, verbose=0)
