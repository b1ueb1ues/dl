from core.simulate import test_with_argv
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Tobias

class Tobias(Adv):
    a1 = ('bt',0.25)
    a3 = ('k_poison',0.3)

    conf = {}
    conf['slots.a'] = RR()+A_Dogs_Day()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `s1
    """

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
        del self.slots.c.ex['blade']
        self.slots.c.ex['tobias'] = ('ex', 'tobias')

    def prerun(self):
        self.s2_mode = 0
        self.s1.autocharge_init(0)
        self.s2.autocharge_init(1).on()
        # self.s2_x_alt = X_alt(self, 'appetizer', appetizer_conf, x_proc=self.l_stance_x, no_fs=True, no_dodge=True)

    def s1_autocharge_off(self, t):
        self.s1.autocharge_timer.off()

    # def s2_x_alt_off(self, t):
        # self.s2_x_alt.off()

    def s1_proc(self, e):
        self.buff_class('s1',0.3,15).on()

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.conf.s2.startup = 0.1
            self.conf.s2.recovery = 1.9
            # self.s2_x_alt.on()
            self.s1.autocharge_timer.on()
            Timer(self.s1_autocharge_off).on(7)
            # Timer(self.s2_x_alt_off).on(10)
        else:
            self.dmg_make('s2',0)
            self.afflics.poison('s2', 120, 0.582)
            self.conf.s2.startup = 0.25
            self.conf.s2.recovery = 0.9
            # self.s2_x_alt.off()
        self.s2_mode = (self.s2_mode + 1) % 2

if __name__ == '__main__':
    test_with_argv('t_hope', *sys.argv)
