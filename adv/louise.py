import adv_test
import adv
from slot.a import *

def module():
    return Louise

class Louise(adv.Adv):
    comment = ''
    a1 = ('od',0.13)

    def pre(this):
        this.conf.mod = {'ex':('sp','passive',0.15)}
        this.conf['slot.a'] = FB()+SS()
        if this.condition('rollfs'):
            this.conf['acl'] = """
                `s1,fsc
                `s2,fsc
                `s3,fsc
                `dodge, fsc
                `fs
                """
        else:
            this.conf['acl'] = """
                `s1
                `s2
                `s3
                """


    def init(this):
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)



if __name__ == '__main__':
    module().comment = 'poison*3'
    conf = {}
    adv_test.test(module(), conf, verbose=0)
