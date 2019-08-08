if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

from adv import *

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


    def init(this):
        if this.condition('big hitbox'):
            this.s1_addition = 4
        else:
            this.s1_addition = 1

        if this.condition('80 resist'):
            this.afflics.sleep.resist=80
        else:
            this.afflics.sleep.resist=100


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



    def s2_before(this, e):
        r = this.afflics.sleep.get()
        coef = 1.40*5 * (1-r)
        return coef

    def s2_proc(this, e):
        r = this.afflics.sleep.get()
        coef = 1.40*5 * r
        this.dmg_make('s2',coef)
        coef = (2.80-1.40)*5 * r
        this.dmg_make('o_s2_boost',coef)




if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

