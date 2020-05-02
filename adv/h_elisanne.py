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
        self.stance = 0

    def s1latency(self, e):
        Teambuff("s1_buff",0.1,15).on()

    def s1_proc(self, e):
        if self.stance == 0:
            self.stance = 1
        elif self.stance == 1:
            Timer(self.s1latency).on(2.5)
            self.stance = 2
        elif self.stance == 2:
            Timer(self.s1latency).on(2.5)
            self.stance = 0

    def s2_proc(self, e):
        self.charge('s2',500)



if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)