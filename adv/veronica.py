from core.advbase import *

def module():
    return Veronica

class Veronica(Adv):
    a3 = ('prep','100%')
    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        """
    coab = ['Ieyasu','Curran','Berserker']

    def prerun(self):
        Teambuff('last',2.28,1).on()
        self.hp = 80

    def s1_proc(self, e):
        with CrisisModifier('s1', 1.25, self.hp):
            self.dmg_make('s1', 10.84)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)