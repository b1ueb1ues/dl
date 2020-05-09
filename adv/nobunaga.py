from core.advbase import *
from slot.a import *
#from slot.d import *

def module():
    return Nobunaga

class Nobunaga(Adv):
    comment = 'use s2 instead of fs to dispel when possible'

    a1 = ('a',0.2,'hit15')

    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['slots.burn.a'] = Resounding_Rendition()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1
        `s2, self.ba
        `fs, x=5 and s2.charged<s2.sp-self.sp_val(2)
        """
    coab = ['Wand','Marth','Serena']

    def prerun(self):
        self.ba = 0
    
    def s1_proc(self, e):
        self.ba = self.dmg_formula('s', 11.18)

    def s2_proc(self, e):
        if self.ba > 0:
            self.dmg_make('o_s1_boost', self.ba, fixed=True)
            self.ba = 0
            self.dmg_make('o_s2_boost',self.conf.s2.dmg*0.3)

    def fs_proc(self, e):
        if self.ba > 0:
            self.dmg_make('o_s1_boost', self.ba, fixed=True)
            self.ba = 0

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)