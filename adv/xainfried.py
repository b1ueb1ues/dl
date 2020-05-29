from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Xainfried

class Xainfried(Adv):
    a1 = ('dc', 4)
    a3 = ('dt', 0.25)
    conf = {}
    conf['slots.a'] = Heralds_of_Hinomoto()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2
        `fs, x=5
        """
    coab = ['Xander', 'Pipple', 'Bow']
    conf['afflict_res.frostbite'] = 0

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.30, ['frostbite']):
            self.dmg_make(e.name, 2.30)
            self.hits += 1
            self.afflics.frostbite(e.name,120,0.41)
            self.dmg_make(e.name, 6.90)
            self.hits += 3

    def s2_proc(self, e):
        self.dragonform.charge_gauge(10)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
