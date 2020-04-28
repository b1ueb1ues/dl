from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Kleimann

class Kleimann(Adv):
    a3 = ('s',0.35)
 
    conf = {}
    conf['slots.a'] = Candy_Couriers()+The_Fires_of_Hate()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        #`fs, not self.madness_status and self.madness > 0
        """
    coab = ['Ieyasu','Bow','Dagger']

    def madness_autocharge(self, t):
        for s in (self.s1, self.s2, self.s3):
            if s.charged < s.sp:
                sp = 100
                s.charge(sp)
                log('sp', s.name+'_autocharge', int(sp))

    def prerun(self):
        self.madness = 0
        self.madness_status = False
        self.madness_timer = Timer(self.madness_autocharge, 2.9, 1)

    def fs_proc(self, e):
        if not self.madness_status:
            self.madness_status = True
            self.madness_timer.on()
        else:
            self.madness_status = False
            self.madness_timer.off()

    def s1_proc(self, e):
        self.afflics.poison('s1',120,0.582)

    def s2_proc(self, e):
        self.afflics.sleep('s2',110)
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make("s2", 11.00)
        if self.madness < 5:
            self.madness += 1

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)