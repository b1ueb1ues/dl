from core.advbase import *
from slot.d import *
from slot.a import *
def module():
    return Chelsea

class Chelsea(Adv):
    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.a'] = Mega_Friends()+Primal_Crisis()
    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=1
    """
    coab = ['Blade', 'Grace', 'Serena']

    def prerun(self):
        self.obsession = 0
        self.s2_buffs = []

        self.a1atk = Selfbuff('a1atk',0.20,-1,'att','passive')
        self.a1spd = Spdbuff('a1spd',0.10,-1)
        self.a3 = Selfbuff('a3_str_passive',0.3,60,'att','passive')

        Event('dragon').listener(self.s2_clear)

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.a3 = Dummy()
        adv.a1atk = Dummy()
        adv.a1spd = Dummy()

    def s2_clear(self, e):
        for buff in self.s2_buffs:
            buff.off()
        self.s2_buffs = []
        self.a3.off()
        self.obsession = 0

    def dmg_before(self, name):
        new_hp = self.hp
        if name != 's1' and self.a3.get():
            new_hp -= 3 * self.obsession
        self.update_hp(new_hp)

    def dmg_proc(self, name, amount):
        new_hp = self.hp
        if name == 's1' and self.a3.get():
            new_hp += 7
        self.update_hp(new_hp)

    def s1_proc(self, e):
        for _ in range(7):
            self.dmg_make(e.name,1.36)
            self.hits += 1

    def update_hp(self, new_hp):
        if new_hp <= 30:
            self.a1atk.on()
            self.a1spd.on()
        else:
            self.a1atk.off()
            self.a1spd.off()
        self.set_hp(new_hp)

    def s2_proc(self, e):
        self.s2_buffs.append(Selfbuff(e.name,0.3,60).on())
        self.obsession = Selfbuff(e.name).stack()
        self.a3.on()

    def dmg_make(self, name, dmg_coef, dtype=None, fixed=None):
        if dtype == None:
            dtype = name
        self.dmg_before(name)
        count = self.dmg_formula(dtype, dmg_coef)
        log('dmg', name, count)
        self.dmg_proc(name, count)
        return count

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)