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

    def l_dodge(this, e):
        this.think_pin('dodge')

    def init(this):
        this.a_dodge.cancel_by = ['fs']
        adv.Listener('dodge',this.l_dodge)


        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s1_poison",2.91)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.dmg_make("o_s2hitpoison",(4.035-2.69)*3)
        this.conf.rotation = """
fs d 
fs d 
fs d 
fs d 
fs d 
fs -------- s1 fs d 
fs d 
fs d 
fs -------- s2 s1
fs d 
fs d 
fs d 
fs -------- s3 fs d 
fs -------- s1 fs d 
fs d 
fs -------- s2 fs d 
fs -------- s1 fs d 
fs d 
fs d 
fs d 
fs -------- s1 s3
fs d 
fs -------- s2 fs d 
fs d 
fs -------- s1 fs d 
fs d 
fs d 
fs d 
fs -------- s1 s2
fs d 
fs d 
fs d 
fs -------- s3 s1
fs d 
fs d 
fs d 
fs d 
fs d 
fs -------- s1 s2
fs d 
fs d 
fs d 
fs d 
fs -------- s1 fs d 
fs -------- s3 fs d 
fs d 
fs -------- s1 s2
fs d 
fs d 
fs d 
fs d 
fs -------- s1 fs d 
fs d 
fs d 
fs d 
fs -------- s1 s2
s3
fs d 
fs d 
fs d 
fs d 
fs -------- s1 fs d 
fs d 
fs d 
fs d 
fs -------- s1 s2
fs d 
fs d 
fs d 
fs -------- s3 s1
fs d 
fs d 
fs d 
fs d 
fs d 
fs -------- s1 
        """






if __name__ == '__main__':
    module().comment = 'poison 3 times & no fs'
    conf = {}
    conf['acl'] = """
        `rotation
        """
    from slot.a import *
    conf['slots.a'] = Stellar_Show() + Forest_Bonds()
    adv_test.test(module(), conf, verbose=0)




['fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 's2', 's1', 'fs', 'fs', 'fs', 'fs', 's3', 'fs', 'fs', 's1', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's3', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs']


['fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 's2', 's1', 'fs', 'fs', 'fs', 'fs', 's3', 'fs', 'fs', 's1', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's3', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2']
