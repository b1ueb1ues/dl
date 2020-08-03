from core.advbase import *
from slot.a import *
from slot.d import *


def module():
    return Summer_Celliera


class Summer_Celliera(Adv):
    a1 = ('bc', 0.15)
    a3 = ('bt', 0.35)
    conf = {}
    conf['slots.a'] = Valiant_Crown() + Proper_Maintenance()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s2
        `s3
        `s4, fsc
        `s1, fsc
        `fs, x=2
        """
    coab = ['Blade', 'Renee', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100
    share = ['Patia', 'Summer_Luca']

    def init(self):
        self.phase['s2'] = 0
        self.celery_s1_bog = 120
        self.celery_s1_hits = 5

    def s1_proc(self, e):
        self.dmg_make(e.name, 1.84)
        self.afflics.bog.on(e.name, 120)
        self.dmg_make(e.name, 1.84*5)

    def s2_proc(self, e):
        self.phase[e.name] += 1
        Teambuff(f'{e.name}_def', 0.15, 10, 'defense').on()
        if self.phase[e.name] > 1:
            Teambuff(e.name, 0.13, 10).on()
        if self.phase[e.name] > 2:
            Spdbuff(f'{e.name}_spd', 0.25, 10, wide='team').on()
        self.phase[e.name] %= 3


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
