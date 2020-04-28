from core.advbase import *

def module():
    return Kirsty

class Kirsty(Adv):
    a3 = ('k_poison',0.3)

    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, seq=5
        """
    coab = ['Blade','Dragonyule_Xainfried','Akasha']

    def prerun(self):
        if self.condition('maintain Dauntless Strength'):
            Timer(self.dauntless_strength).on(15)
            Timer(self.dauntless_strength).on(30)
            Timer(self.dauntless_strength).on(45)

    def dauntless_strength(self, t):
        Selfbuff('dauntless_strength',0.20,-1).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)