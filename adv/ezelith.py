from core.advbase import *
from slot.d import *

def module():
    return Ezelith

class Ezelith(Adv):
    comment = ''
    a3 = ('bk',0.35)
    conf = {}
    conf['slots.d'] = Gala_Mars()
    conf['acl'] = """
        `dragon, s=1
        `s3, not self.s3_buff
        `s1
        `s2, cancel
        `fs, x=5
        """
    coab = ['Halloween_Mym', 'Blade', 'Marth']

    def prerun(self):
        self.s2_buff = Selfbuff('s2',0.2,15)
        self.s1_hit_frames = [13, 13, 20, 28, 10, 19, 26, 10, 16, 24, 44]
        self.a1_on = True
        self.a1_hits = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s1_hit_frames = [13, 13, 20, 28, 10, 19, 26, 10, 16, 24, 44]
        adv.rebind_function(Ezelith, 's1_hit')
        adv.a1_on = False
        adv.a1_hits = 0

    def s2_chance(self):
        if self.hits >= 15:
            return 0.35
        else:
            return 0.15

    def s1_hit(self, t):
        self.dmg_make(t.name,t.dmg_coef,'s')
        self.a1_hits += 1
        self.hits += 1
        if self.a1_on and self.a1_hits % 2 == 0:
            Selfbuff('a1',0.2,7,'crit','chance').on()

    def s1_proc(self, e):
        f_sum = 0
        for f in self.s1_hit_frames[0:-1]:
            f_sum += f
            t_s1 = Timer(self.s1_hit)
            t_s1.name = e.name
            t_s1.dmg_coef = 0.63
            t_s1.on(f_sum/60)
        f_sum += self.s1_hit_frames[-1]
        t_s1 = Timer(self.s1_hit)
        t_s1.name = e.name
        t_s1.dmg_coef = 4.00
        t_s1.on(f_sum/60)

    def s2_proc(self, e):
        self.s2_buff.on()

    # def dmg_proc(self, name, amount):    
    #     if name[0] == 'x' and self.s2_buff.get():
    #         r = random.random()
    #         if r < self.s2_chance():
    #             Debuff("s2_ab",0.05,5,1).on()

    def dmg_proc(self, name, amount):
        if name[0] == 'x' and self.s2_buff.get():
            Debuff('s2_ab', 0.05, 5, self.s2_chance()).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)