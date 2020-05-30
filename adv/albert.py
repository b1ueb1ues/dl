from core.advbase import *
import copy
from module.x_alt import Fs_alt

def module():
    return Albert

class Albert(Adv):
    a1 = ('fs',0.5)
    conf = {}
    conf['acl'] = """
        `dragon, fsc
        `s2, s1.charged>=s1.sp-330
        `fs, s=2 and not self.afflics.paralysis.get()
        `s1, fsc
        `s3, fsc
        `fs, seq=2
        """
    coab = ['Blade','Dagger','Peony']
    conf['afflict_res.paralysis'] = 0

    def fs_proc_alt(self, e):
        self.afflics.paralysis('fs',100,0.803)

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg':1.02,
            'fs.sp':330,
            'fs.recovery':26/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        self.s2.autocharge_init(self.s2autocharge).on()
        self.s2buff = Selfbuff("s2_shapshift",1, 20,'ss','ss')
        self.a3 = Selfbuff('a2_str_passive',0.25,20,'att','passive')

        self.fs_alt_timer = Timer(self.fs_alt_end)
        self.s1_hits = 6 if self.condition('big hitbox') else 4

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s2buff = Dummy()

    def fs_alt_end(self,t):
        self.fs_alt.off()

    def s2autocharge(self, t):
        if not self.s2buff.get():
            self.s2.charge(160000.0/40)
            log('sp','s2autocharge')

    def s1_proc(self, e):
        if self.s2buff.get():
            name = f'o_{e.name}_boost'
            self.dmg_make(name,12.38-0.825)
            for _ in range(2, self.s1_hits+1):
                self.dmg_make(name, 0.83)
                self.hits += 1
            self.s2buff.buff_end_timer.timing += 2.6
            self.a3.buff_end_timer.timing += 2.6

    def s2_proc(self, e):
        self.s2buff.on()
        self.a3.on()
        self.fs_alt.on(-1)
        self.fs_alt_timer(20)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)