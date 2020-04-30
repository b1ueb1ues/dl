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
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def c_s2_proc(self, e):
        Teambuff('s2',0.15,15).on()

    def s2_proc(self, e):
        Selfbuff('s2',0.15,15).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)