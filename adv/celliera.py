from core.advbase import *
from slot.a import *

def module():
    return Celliera

class Celliera(Adv):
    a3 = ('a',0.08,'hp70')

    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2, seq=5
        `s3
    """
    coab = ['Dagger', 'Xander', 'Summer_Estelle']

    def prerun(self):
        self.s2buff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        self.s2str = Selfbuff("s2_str",0.25,10)

    def s1_proc(self, e):
        if self.s2buff.get():
            self.s2buff.buff_end_timer.timing += 2.5
            self.s2str.buff_end_timer.timing += 2.5

    def s2_proc(self, e):
        self.s2buff.on()
        self.s2str.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)