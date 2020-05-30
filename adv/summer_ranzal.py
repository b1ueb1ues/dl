from core.advbase import *
from slot.a import *
from slot.d import*

def module():
    return Summer_Ranzal

class Summer_Ranzal(Adv):
    a1 = ('lo',0.4)
    a3 = ('primed_defense', 0.08)

    conf = {}
    conf['slots.a'] = RR() + Breakfast_at_Valerios()
    conf['slots.frostbite.a'] = PC() + His_Clever_Brother()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1, x=5
        `s2, x=5
        `s3
        """
    coab = ['Xander', 'Dagger', 'Tiki']
    conf['afflict_res.bog'] = 100

    def init(self):
        self.a3_iscding = 0
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff

    def s1_proc(self, e):
        self.dmg_make(e.name,2.16)
        self.afflics.bog.on(e.name, 100)
        self.dmg_make(e.name,6.48)

    def s2_proc(self, e):
        self.buff_class(e.name,0.10,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
