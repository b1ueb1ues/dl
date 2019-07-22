import adv_test
import adv

def module():
    return Louise

class Louise(adv.Adv):
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
        this.conf.rotation = """
fs d 
fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d -------- s2 fs d -------- s1 fs d 
fs d 
fs d -------- s3 fs d 
fs d -------- s1 fs d 
fs d 
fs d -------- s2 fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s3 fs d -------- s2 fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d -------- s3 fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d -------- s3 fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d -------- s3 fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s3 fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d
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
