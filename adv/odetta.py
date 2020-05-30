from core.advbase import *

def module():
    return Odetta

class Odetta(Adv):
    comment = 'c2+fs'

    conf = {}
    conf['acl'] = """
        `dragon
        `s2, fsc
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """
    coab = ['Blade','Dagger','Peony']

    a1 = ('a',0.1,'hp70')
    a3 = ('bt',0.2)

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.buff_class(e.name,0.15,15).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)