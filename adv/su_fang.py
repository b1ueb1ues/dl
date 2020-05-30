from core.advbase import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Su_Fang

class Su_Fang(Adv):
    a3 = ('s',0.35)
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, fsc
        `s1
        `fs, x=4
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']

    def fs_proc_alt(self, e):
        self.afflics.poison('fs', 120, 0.582)

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 0.174, 'fs.hit': 6}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2_buff = Selfbuff('s2', 0.30, 15)

    def s1_proc(self, e):
        with KillerModifier('skiller', 'hit', 0.50, ['poison']):
            self.dmg_make(e.name, 5.58)
            if self.s2_buff.get():
                self.dmg_make(e.name, 2.60)
                self.hits += 2

    def s2_proc(self, e):
        self.fs_alt.on(1)
        self.s2_buff = Selfbuff(e.name, 0.30, 15).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
