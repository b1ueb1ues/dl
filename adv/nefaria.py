from core.advbase import *
from module.x_alt import Fs_alt
from slot.a import *

def module():
    return Nefaria

class Nefaria(Adv):
    comment = 's2 fs(precharge) s1 s1'
    
    a1 = [('edge_blind', 60, 'hp100'),('edge_poison', 60, 'hp100')]
    a3 = [('k_blind',0.4), ('k_poison',0.3)]

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `fs, self.fs_alt.uses > 0 and x=4
        `s1, fsc or x=1 or not self.s3_buff
        `s2
        """
    coab = ['Wand','Gala_Alex','Heinwald']

    conf['afflict_res.blind'] = 80
    conf['afflict_res.poison'] = 0

    def fs_proc_alt(self, e):
        self.afflics.blind('s2_fs', 110)
    
    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':7.90,
            'fs.hit':19,
            'fs.sp':2400,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        
    def s1_proc(self, e):
        with KillerModifier('s1killer', 'hit', 0.74, ['blind', 'poison']):
            self.dmg_make(e.name,1.06)
            self.hits += 1
            self.afflics.poison(e.name, 70, 0.582)
            self.dmg_make(e.name,7*1.06)
            self.hits += 7

    def s2_proc(self, e):
        self.fsacharge = 1
        self.fs_alt.on(1)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)