from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

def module():
    return Xander

class Xander(Adv):
    comment = 'c2+fs'

    a3 = ('fs',0.55)

    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end'), fsc
        `s3
        `s1
        `s2
        `s4
        `fs, x=2 and (self.fs_alt.uses=0 or self.fs_alt.uses=2)

        # use FS instead of S1 P3
        # `fs, x=2 and (self.fs_alt.uses=0 or self.fs_alt.uses=2)
    """
    coab = ['Blade', 'Yurius', 'Hunter_Sarisse']
    share = ['Gala_Elisanne', 'Ranzal']

    def fs_proc_alt(self, e):
        if self.fs_alt.uses == 2:
            with KillerModifier('fs_killer', 'hit', 0.30, ['frostbite']):
                self.dmg_make('fs', 6.66)
        else:
            self.dmg_make('fs', 3.26)
        self.conf[e.name].dmg = 8.32
        self.fs_alt.off()
        self.born_ruler.off()

    def prerun(self):
        # identical to granzal FS in frames
        conf_fs_alt = {
            'fs.dmg': 0.0,
            'fs.sp': 330,
            'fs.hit': 3,

            'fs.charge': 2/60.0, # needs confirm
            'fs.startup': 66/60.0,
            'x1fs.startup': 75/60.0,
            'x2fs.startup': 60/60.0,
            'x3fs.startup': 60/60.0,

            'fs.recovery': 13/60.0,
            'x1fs.recovery': 13/60.0,
            'x2fs.recovery': 13/60.0,
            'x3fs.recovery': 13/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.born_ruler = Selfbuff('born_ruler', 0.05, -1, 'att', 'buff')
    
    def s1_proc(self, e):
        boost = 0.05*self.buffcount
        self.afflics.frostbite(e.name,120,0.41*(1+boost))
        try:
            if self.fs_alt.get():
                self.fs_alt.uses += 1
                if self.fs_alt.uses == 2:
                    # phase 2
                    self.dmg_make(f'o_{e.name}_boost',self.conf[e.name].dmg*boost)
                    self.conf[e.name].dmg = 8.40
                elif self.fs_alt.uses == 3:
                    # phase 3
                    self.dmg_make(f'o_{e.name}_boost',self.conf[e.name].dmg*boost)
                    self.conf[e.name].dmg = 8.32
                    self.fs_alt.off()
                    self.born_ruler.off()
            else:
                self.fs_alt.on()
                self.born_ruler.on()
                # phase 1
                self.dmg_make(f'o_{e.name}_boost',self.conf[e.name].dmg*boost)
                self.conf[e.name].dmg = 8.37
        except:
            self.dmg_make(f'o_{e.name}_boost',self.conf[e.name].dmg*boost)

    def s2_proc(self, e):
        self.dmg_make(f'o_{e.name}_boost',self.conf[e.name].dmg*0.05*self.buffcount)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
