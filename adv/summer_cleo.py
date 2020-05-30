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
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(self, dst):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s1_lantency(self, t):
        self.dmg_make(t.name,1.06)
        self.hits += 1
        p = self.afflics.paralysis(t.name,120,0.97)
        self.afflics.paralysis.get()
        if random.random() < p :
            Selfbuff('a1',0.10,20,'sp','passive').on()
        self.dmg_make(t.name,1.06)
        self.hits += 1
        self.dmg_make(t.name,1.06)
        self.hits += 1
        self.dmg_make(t.name,5.3)
        self.hits += 1

        for _ in range(min(len(self.all_buffs), 4)):
            self.dmg_make(f'o_{t.name}_boost',1.06)
            self.hits += 1

    def s1_proc(self, e):
        t = Timer(self.s1_lantency)
        t.name = e.name
        t.on(1)

    def s2_proc(self, e):
        self.buff_class(e.name,0.05,10).on()
        self.buff_class(f'{e.name}_crit',0.03,10,'crit','chance').on()
        self.buff_class(f'{e.name}_sd',0.10,10,'s').on()
        self.buff_class(f'{e.name}_sp',0.10,10,'sp','passive').on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)