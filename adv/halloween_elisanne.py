from core.advbase import *
from slot.a import *

def module():
    return Halloween_Elisanne

class Halloween_Elisanne(Adv):
    a1 = ('s',0.3)

    conf = {}
    conf['slots.a'] = Dragon_and_Tamer()+Primal_Crisis()
    conf['slots.paralysis.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2, x=5
        `s3
        `fs, x=5
        """
    coab = ['Blade','Dagger','Peony']

    def prerun(self):
        self.phase['s1'] = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.rebind_function(Halloween_Elisanne, 's1_latency')
        adv.phase[dst] = 0

    def s1_latency(self, t):
        Teambuff(t.name,0.1,15).on()

    def s1_proc(self, e):
        self.phase[e.name] += 1
        if self.phase[e.name] > 1:
            t = Timer(self.s1_latency)
            t.name = e.name
            t.on(2.5)
        self.phase[e.name] %= 3

    def s2_proc(self, e):
        self.charge(e.name,500)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)