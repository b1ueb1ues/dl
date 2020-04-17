import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *
from slot.d import*
def module():
    return Renee

class Renee(Adv):
    a1 = ('primed_crit_chance', 0.6,5)

    conf = {}
    conf['slot.a'] = Twinfold_Bonds()+The_Prince_of_Dragonyule()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3, seq=5
        `fs, seq=5
        """
    coab = ['Blade', 'Xander', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100

    def s1_proc(self, e):
        self.dmg_make('s1',1.11)
        self.afflics.bog.on('s1', 100)
        self.dmg_make('s1',5.55)

    def s2_proc(self, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

