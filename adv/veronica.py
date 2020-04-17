from core.advbase import *
from slot.d import *

def module():
    return Veronica

class Veronica(Adv):
    a3 = ('prep','100%')
    conf = {}
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, (s1.charged>=s1.sp-self.sp_val('fs')) or (s2.charged>=s2.sp-self.sp_val('fs'))
        """

    def prerun(self):
        Teambuff('last',2.28,1).on()
        self.hp = 80

    def s1_proc(self, e):
        with CrisisModifier('s1', 1.25, self.hp):
            self.dmg_make('s1', 10.84)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)