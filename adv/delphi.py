from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Delphi

class Delphi(Adv):
    a1 = ('a',-0.55)

    conf = {}
    conf['slots.a'] = Mega_Friends()+The_Fires_of_Hate()
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, self.s1fscharge == 0 and (s1.charged <= ((s1.sp/13)*9))
        `fs, x=2
    """
    coab = ['Blade','Gala_Alex','Heinwald']
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.flurry_poison = 70
        
        self.s1defdown = self.condition('s1 defdown for 10s')

        self.s1.autocharge_init(80000).on()
        self.s2.autocharge_init(50000).on()
        self.s1fscharge = 0

    def s1_proc(self, e):
        if self.s1defdown:
            buff = Debuff('s1defdown',0.20,10,1)
            buff.bufftime = buff._no_bufftime
            buff.on()
        self.s1fscharge = 1
    
    def s2_proc(self, e):
        self.afflics.poison(e.name,120+self.flurry_poison*(self.hits>=15),3.00,27)

    def fs_proc(self, e):
        if self.s1fscharge > 0:
            self.s1fscharge -= 1
            self.dmg_make("o_fs_boost",0.21*3)
            self.afflics.poison('fs',120+self.flurry_poison*(self.hits>=15),3.00,27)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)