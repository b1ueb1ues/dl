from core.advbase import *

def module():
    return Hanabusa

class Hanabusa(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3
        """
    coab = ['Halloween_Elisanne','Dagger','Peony']

    def prerun(self):
        self.stance = 0

    def s1_proc(self, e):
        if self.stance == 0:
            self.s1.sp = 2567
            self.stance = 1
            Timer(self.stanceend).on(20)
        elif self.stance == 1:
            self.dmg_make(e.name,1.94)
            self.stance = 2
            Timer(self.stanceend).on(20)
        elif self.stance == 2:
            self.dmg_make(e.name,2.51)
            self.s1.sp = 2840
            self.stance = 0

    def s2_proc(self, e):
        if self.stance == 0:
            Teambuff(e.name,0.15,15).on()
        elif self.stance == 1:
            Teambuff(e.name,0.15,18).on()
        elif self.stance == 2:
            Teambuff(e.name,0.15,21).on()

    def stanceend(self, e):
        self.s1.sp = 2840
        self.stance = 0

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)