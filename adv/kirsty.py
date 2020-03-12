from core.advbase import *

def module():
    return Kirsty

class Kirsty(Adv):
    a3 = ('k_poison',0.3)

    comment = 'no poison'
    conf = {}
    conf['slot.d'] = slot.d.Garland()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        """

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