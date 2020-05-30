from core.advbase import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Lin_You

class Lin_You(Adv):
    a1 = [('cc',0.10,'hp70'), ('cc',0.20,'hit25'), ('cc',0.20,'hit50')]
    a3 = ('sp',0.08)
    conf = {}
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s2, s1.check()
        `s1
        `fs, self.hits <= 44 and self.fs_alt.uses > 0 and x=4
        """
    coab = ['Blade','Dragonyule_Xainfried','Axe2']

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 2.59, 'fs.hit': 6}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))
        self.s2_buff = Spdbuff('s2_spd',0.20, 15)

    def s1_proc(self, e):
        if self.s2_buff.get():
            self.dmg_make(f'{e.name}_powerup', 1.86*3)
            self.s2_buff.buff_end_timer.add(self.s1.ac.getstartup()+self.s1.ac.getrecovery())
            self.hits += 3
            self.afflics.sleep(e.name, 150)
        self.fs_alt.on(3)

    def s2_proc(self, e):
        self.s2_buff.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)