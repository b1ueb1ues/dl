import adv_test
import adv

def module():
    return W_Aoi

class W_Aoi(adv.Adv):
    comment = ''
    a3 = ('sp',0.1,'fs')


    def pre(this):
        if this.condition('big hitbox'):
            this.s1_addition = 4
        else:
            this.s1_addition = 1

    def init(this):
        this.sleep_last = 0
        if this.condition('sleep*3'):
            this.sleep_last = 3
            this.dmg_make('o_s2boost',1.33*5)
            this.dmg_make('o_s2boost',1.33*5)
            this.dmg_make('o_s2boost',1.33*5)

        #this.conf.s1.dmg += this.s1_addition * 1.47
        
        this.fsa_charge = 0

    def s1_proc(this, e):
        if this.s1_addition == 4:
            this.dmg_make('o_s1_hit1',1.47)
            this.dmg_make('o_s1_hit2',1.47)
            this.dmg_make('o_s1_hit3',1.47)
            this.dmg_make('o_s1_hit4',1.47)
        elif this.s1_addition == 1:
            this.dmg_make('o_s1_hit1',1.47)

        

    def s1_before(this, e):
        if this.sleep_last > 0:
            this.sleep_last -= 1
            adv.Teambuff('a1',0.15,10).on()




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

