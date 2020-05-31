from core.advbase import *

def module():
    return Irfan

class Irfan(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5
        `s3
        `fs, seq=5
        """
    coab = ['Blade','Halloween_Elisanne','Peony']

    def s2_proc(self, e):
        Debuff(e.name, 0.05, 10, 0.8, 'attack').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)