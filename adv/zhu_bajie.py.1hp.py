from core.advbase import *
import adv.zhu_bajie

def module():
    return Zhu_Bajie

class Zhu_Bajie(adv.zhu_bajie.Zhu_Bajie):
    conf = adv.zhu_bajie.Zhu_Bajie.conf.copy()

    def prerun(self):
        super().prerun()
        self.set_hp(0)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Zhu_Bajie, *sys.argv)