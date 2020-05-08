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
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc

    def s1_proc(self, e):
        self.dmg_make('s1',2.16)
        self.afflics.bog.on('s1', 100)
        self.dmg_make('s1',6.48)

    def c_s2_proc(self, e):
        Teambuff('s2',0.10,15).on()

    def s2_proc(self, e):
        Selfbuff('s2',0.10,15).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)