import adv.adv_test
from adv import *
from slot.d import *

def module():
    return Ezelith

class Ezelith(Adv):
    comment = ''
    a3 = ('bk',0.35)
    conf = {}
    conf['slot.d'] = Arctos()
    conf['acl'] = """
        `dragon
        `s3, not this.s3_buff_on
        `s1
        `s2, seq=4
        `fs, seq=5
        """


    def prerun(this):
        random.seed()
        this.s2_buff = Selfbuff('s2',0.2,15)
        this.s1_hit_frames = [13, 13, 20, 28, 10, 19, 26, 10, 16, 24, 44]
        this.a1_hits = 0

    def s2_chance(this):
        if this.hits >= 15:
            return 0.35
        else:
            return 0.15

    def s1_hit(this, t):
        this.dmg_make('s1',t.dmg_coef,'s')
        this.a1_hits += 1
        this.hits += 1
        if this.a1_hits % 2 == 0:
            Selfbuff('a1',0.2,7,'crit','chance').on()

    def s1_proc(this, e):
        f_sum = 0
        for f in this.s1_hit_frames[0:-1]:
            f_sum += f
            t_s1 = Timer(this.s1_hit)
            t_s1.dmg_coef = 0.63
            t_s1.on((f_sum+3)/60)
        f_sum += this.s1_hit_frames[-1]
        t_s1 = Timer(this.s1_hit)
        t_s1.dmg_coef = 4.00
        t_s1.on((f_sum+3)/60)

    def s2_proc(this, e):
        this.s2_buff.on()

    def dmg_proc(this, name, amount):    
        if name[0] == 'x' and this.s2_buff.get():
            r = random.random()
            if r < this.s2_chance():
                Debuff("s2_ab",0.05,5,1).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, mass=1, verbose=-2)