from core.simulate import test_with_argv
from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import Fs_alt

def module():
    return Lin_You

class Lin_You(Adv):
    comment = '2in1 ' 
    a1 = [('cc',0.10,'hp70'), ('cc',0.20,'hit25'), ('cc',0.20,'hit50')]
    a3 = ('sp',0.08)
    conf = {}
    conf['slot.d'] = Long_Long()
    conf['slot.a'] = The_Wyrmclan_Duo()+Primal_Crisis()
    conf['acl'] = """
        `s2, s1.check()
        `s1
        `s3, x=5
        """

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 2.42, 'fs.hit': 5}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))
        self.s2_buff = Spdbuff('s2_spd',0.20, 15)

    def s1_proc(self, e):
        if self.s2_buff.get():
            self.dmg_make('s1_powerup', 1.86*3)
            self.s2_buff.buff_end_timer.add(self.s1.ac.getstartup()+self.s1.ac.getrecovery())
            self.hits += 3
            self.afflics.sleep('s1', 150)
        self.fs_alt.on(3)

    def s2_proc(self, e):
        self.s2_buff.on()

if __name__ == '__main__':
    test_with_argv('t_hope', *sys.argv)