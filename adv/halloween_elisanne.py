from core.advbase import *
from slot.a import *

def module():
    return Halloween_Elisanne

class Halloween_Elisanne(Adv):
    a1 = ('s',0.35)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['slots.paralysis.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon, fsc
        `s2
        `s1
        `s3, x=5
        `fs, x=5
        """
    coab = ['Blade','Sharena','Peony']
    conf['afflict_res.paralysis'] = 0

    def prerun(self):
        self.phase['s1'] = 0
        self.heli_s1_sp = {0: 4548, 1: 5499, 2: 6145}

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.rebind_function(Halloween_Elisanne, 's1_latency')
        adv.phase[dst] = 0
        adv.heli_s1_sp = {0: 6822, 1: 12097, 2: 13826}

    def s1_latency(self, t):
        Teambuff(t.name,0.13,15).on()

    def s1_proc(self, e):
        self.phase[e.name] += 1
        with KillerModifier(e.name, 'hit', 0.2 * int(self.phase[e.name] == 3), ['paralysis']):
            self.dmg_make(e.name, 1.17)
            if self.phase[e.name] > 1:
                t = Timer(self.s1_latency)
                t.name = e.name
                t.on(2.5)
                self.afflics.paralysis(e.name, 120, 0.97)
            self.dmg_make(e.name, 1.17*6)
        self.phase[e.name] %= 3
        self.conf[e.name].sp = self.heli_s1_sp[self.phase[e.name]]
        self.__getattribute__(e.name).sp = self.heli_s1_sp[self.phase[e.name]]

    def s2_proc(self, e):
        self.charge(e.name, 700)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)