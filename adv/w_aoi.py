import adv.adv_test
from core.advbase import *

def module():
    return W_Aoi

class W_Aoi(Adv):
    comment = ''
    a3 = ('sp',0.12,'fs')
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=5
        """
    conf['afflict_res.sleep'] = 80

    def init(this):
        if this.condition('big hitbox'):
            this.s1_addition = 4
        else:
            this.s1_addition = 1

    def s1_before(this, e):
        this.dmg_make('o_s1_hit1',1.47)
        this.afflics.sleep('s1',110,6.5)
        Teambuff('a1',0.15*this.afflics.sleep.get(),10).on()

    def s1_proc(this, e):
        if this.s1_addition == 4:
            this.dmg_make('o_s1_hit2',1.47)
            this.dmg_make('o_s1_hit3',1.47)
            this.dmg_make('o_s1_hit4',1.47)
        elif this.s1_addition == 1:
            pass


    def s2_proc(this, e):
        with Modifier("s1killer", "sleep_killer", "hit", 1):
            this.dmg_make('s1',5*1.40)




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

