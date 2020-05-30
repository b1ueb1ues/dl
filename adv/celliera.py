from core.advbase import *
from slot.d import *
from slot.a import *
from module.x_alt import *

def module():
    return Celliera

class Celliera(Adv):
    a3 = ('lo',0.50)

    conf = {}
    conf['slots.d'] = Siren()
    conf['slots.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['acl'] = """
        `s2, not self.s2_buff.get()
        `s1
        `s3, cancel
    """
    coab = ['Dagger', 'Xander', 'Wand']

    def prerun(self):
        self.s2_buff = Selfbuff('s2',0.25,-1,'att','buff')
        self.frostbite = Timer(self.frostbite_damage, timeout=2.9, repeat=True)

    def frostbite_damage(self, t):
        if self.hp > 0:
            self.set_hp(self.hp-1)

    def fs_proc(self, e):
        if self.s2_buff.get():
            self.afflics.freeze(100)
            self.frostbite.off()
            self.s2_buff.off()

    def s1_proc(self, e):
        if self.s2_buff.get():
            self.afflics.frostbite(e.name,120,0.37)

    def s2_proc(self, e):
        if self.s2_buff.get():
            self.dragonform.disabled = False
            self.frostbite.off()
            self.s2_buff.off()
        else:
            self.dragonform.disabled = True
            self.frostbite.off()
            self.s2_buff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)