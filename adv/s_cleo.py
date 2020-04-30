from core.advbase import *
from slot.a import *

def module():
    return Summer_Cleo

class Summer_Cleo(Adv):
    comment = 'nofs'

    a3 = ('k_paralysis',0.3)

    conf = {}
    conf['slots.a'] = RR()+Spirit_of_the_Season()
    conf['acl'] = """
            `dragon
            `s2
            `s1
            `s3
            """
    coab = ['Blade','Sharena','Peony']
    conf['afflict_res.paralysis'] = 0

    def init(self):
        random.seed()
        self.bc = Selfbuff()
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def s1_lantency(self, t):
        self.dmg_make('s1_missile',1.06)
        self.hits += 1
        p = self.afflics.paralysis('s1',120,0.97)
        buffcount = self.bc.buffcount()
        self.afflics.paralysis.get()
        if random.random() < p :
            Selfbuff('a1',0.10,20,'sp','passive').on()
        self.dmg_make('s1_missile',1.06)
        self.hits += 1
        self.dmg_make('s1_missile',1.06)
        self.hits += 1
        self.dmg_make('s1_big_missile',5.3)
        self.hits += 1

        if buffcount > 4:
            buffcount = 4
        for i in range(buffcount):
            self.dmg_make('o_s1_boost',1.06)
            self.hits += 1

    def s1_proc(self, e):
        Timer(self.s1_lantency).on(1)

    def c_s2_proc(self, e):
        Teambuff('s2str',0.05,10).on()
        Teambuff('s2crit',0.03,10,'crit','chance').on()
        Teambuff('s2sd',0.10,10,'s').on()
        Teambuff('s2sp',0.10,10,'sp','passive').on()

    def s2_proc(self, e):
        Selfbuff('s2str',0.05,10).on()
        Selfbuff('s2crit',0.03,10,'crit','chance').on()
        Selfbuff('s2sd',0.10,10,'s').on()
        Selfbuff('s2sp',0.10,10,'sp','passive').on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)