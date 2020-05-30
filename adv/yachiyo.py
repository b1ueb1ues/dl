from core.advbase import *
from slot.a import *
from slot.w import *

class w530(WeaponBase):
    ele = ['water','light']
    wt = 'blade'
    att = 468


def module():
    return Yachiyo

class Yachiyo(Adv):
    a1 = ('affself_paralysis', 0.15, 10, 5)
    a3 = ('k_paralysis', 0.2)

    conf = {}
    conf['slots.a'] = MF()+SotS()
    conf['acl'] = """
        `dragon
        `fs, self.fsa_charge and seq=5
        `s2
        `s1
        `s3, fsc
        """
    coab = ['Malora','Dagger','Peony']
    conf['afflict_res.paralysis'] = 0

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Sharena','Dagger','Peony']

    def prerun(self):
        self.fsa_charge = 0

    def s1_proc(self, e):
        self.dmg_make(e.name,4.32)
        self.afflics.paralysis(e.name,100,0.66)
        self.dmg_make(e.name,4.32)

    def s2_proc(self, e):
        # self.fso_dmg = self.conf.fs.dmg
        self.fso_sp = self.conf.fs.sp
        # self.conf.fs.dmg = 7.82
        self.conf.fs.sp = 200
        self.fsa_charge = 1

    def fs_proc(self, e):
        if self.fsa_charge:
            # self.conf.fs.dmg = self.fso_dmg
            self.dmg_make(f'o_{e.name}_boost',6.90)
            self.conf.fs.sp = self.fso_sp
            self.fsa_charge = 0


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
