from core.advbase import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Hawk

class Hawk(Adv):
    a1 = [('edge_stun', 50), ('edge_poison', 50)]
    a3 = [('k_stun',0.4), ('k_poison',0.3)]
    
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        # queue self.duration<=60 and prep and self.afflics.stun.resist
        # s2; s3; fs; s1, fsc; fs; s1, fsc; s1, cancel; s2, cancel
        # end
        `s3, not self.s3_buff
        `dragon.act('c3 s end'), s and self.duration >= 120
        `s2, self.fs_alt.uses=0 or (self.s2_mode=1)
        `fs, (s1.check() and self.fs_alt.uses>1) or (x=4 and self.s2_mode=0 and self.fs_alt.uses>0)
        `s1, fsc or s=1
    """

    coab = ['Blade','Dragonyule_Xainfried','Sylas']
    conf['afflict_res.stun'] = 80
    conf['afflict_res.poison'] = 0
    
    def fs_proc_alt(self, e):
        self.afflics.stun('fs', 110)
        self.afflics.poison('fs', 120, 0.582)

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg': 4.94,
            'fs.hit':19,
            'fs.sp':2400,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2_mode = 0
        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 2.5}))

    def s1_proc(self, e):
        with KillerModifier('s1_stun_killer', 'hit', 3.3, ['stun']):
            self.dmg_make(e.name,4.74)
        with KillerModifier('s1_poison_killer', 'hit', 2, ['poison']):
            self.dmg_make(e.name,4.74)

    def s2_proc(self, e):
        if self.s2_mode == 0:
            self.fs_alt.on(2)
            self.s2.ac = self.a_s2a
        else:
            with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
                self.dmg_make(e.name, 9.48)
            self.conf.s2.startup = 0.25
            self.conf.s2.recovery = 0.9
            self.s2.ac = self.a_s2
            self.hits += 3
        self.s2_mode = (self.s2_mode + 1) % 2


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
