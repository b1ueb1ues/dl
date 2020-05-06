from core.advbase import *

def module():
    return Fritz

class Fritz(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s1, x=5 and cancel or fsc
        `s2
        `s3
        `fs, x=5
        """
    coab = ['Blade','Halloween_Elisanne','Peony']

    def prerun(self):
        self.stance = 0
        self.s2fscharge = 0

    def s2_proc(self, e):
        self.s2fscharge = 3

    def fs_proc(self, e):
        if self.s2fscharge > 0:
            self.s2fscharge -= 1
            self.dmg_make("o_fs_boost",0.57*3+0.29)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)