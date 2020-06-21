from core.advbase import *
from slot.a import *

def module():
    return Halloween_Elisanne

class Halloween_Elisanne(Adv):
    comment = 'lv90 55mc'
    a1 = ('s',0.3)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['slots.paralysis.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon
        `s1
        `s2, fsc
        `s3
        `fs, x=5
        """
    coab = ['Blade','Wand','Peony']
    
    conf['c.att'] = 521 # lv90 55 mc
    conf['c.lv2_autos'] = False
    conf['s1.dmg'] = 8.05
    conf['s1.sp'] = 2450
    conf['s2.dmg'] = 8.30
    conf['s2.hit'] = 10
    conf['s2.recovery'] = 3.55

    def prerun(self):
        self.phase['s1'] = 0

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
    test_with_argv(Halloween_Elisanne, *sys.argv)