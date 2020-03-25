from core.advbase import *

def module():
    return Norwin

class Norwin(Adv):
    a1 = ('affteam_blind', 0.10, 10, 5)
    a3 = ('k_blind', 0.20)
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1, self.s3_buff
        `s2
    """
    conf['afflict_res.blind'] = 80

    def s1_proc(self, e):
        self.afflics.blind('s1',100)

    def s2_proc(self, e):
        with Modifier("s1killer", "blind_killer", "hit", 0.44):
            self.dmg_make('s1',3*2.45)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)