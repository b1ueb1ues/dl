import adv_test
import adv

def module():
    return Louise

class Louise(adv.Adv):
    comment = 'rollfs'
    a1 = ('od',0.13)

    def pre(this):
        this.conf.mod = {'ex':('sp','passive',0.15)}


    def init(this):
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)



if __name__ == '__main__':
    module().comment = 'poison 3 times'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `dodge, fsc
        `fs
        """
    from slot.a import *
    conf['slots.a'] = Stellar_Show() + Forest_Bonds()
    adv_test.test(module(), conf, verbose=0)
