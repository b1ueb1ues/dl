from core.advbase import *

def module():
    return Lucretia

class Lucretia(Adv):
    a1 = ('energized_att', 0.20)
    a3 = ('bk',0.3)
    conf = {}
    conf['acl'] = """
        `dragon, s=2
        `s2, x=5
        `s1
        `s3
        """
    coab = ['Blade','Dagger','Peony']

    def s1_proc(self, e):
        self.energy.add(1, team=True)

    def s2_proc(self, e):
        self.energy.add(2)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)