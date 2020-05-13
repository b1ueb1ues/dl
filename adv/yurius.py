from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yurius

class Yurius(Adv):
    a3 = ('prep', 100)
    conf = {}
    conf['slots.a'] = Primal_Crisis()+Candy_Couriers()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['slots.frostbite.d'] = Siren()
    conf['acl'] = """
        `dragon, not self.dragondrive_buff.get() and self.inspiration()
        `s2
        `s1
        `s3, cancel
    """
    coab = ['Blade','Dagger','Xander']

    def prerun(self):
        # 3000/1200/75
        self.dragondrive_buff = Selfbuff('dragondrive_sd', 0.35, -1, 's', 'passive')
        self.dragondrive_haste = Selfbuff('dragondrive_sp',0.30, -1, 'sp', 'buff')
        self.dragonform.set_dragondrive(self.dragondrive_buff, drain=75)
        Event('dragon_end').listener(self.dragondrive_on) # cursed
        Event('dragondrive_end').listener(self.dragondrive_off)

    def dragondrive_on(self, e):
        self.dragondrive_haste.on()

    def dragondrive_off(self, e):
        self.dragondrive_haste.off()

    def s1_proc(self, e):
        if self.dragondrive_buff.get():
            with KillerModifier('s1_killer', 'hit', 0.6, ['frostbite']):
                self.dmg_make('s1', 7.92)
        else:
            self.dmg_make('s1', 7.56)
            self.dragonform.charge_gauge(530, utp=True)
            self.inspiration.add(1)

    def s2_proc(self, e):
        if self.dragondrive_buff.get():
            with KillerModifier('s2_killer', 'hit', 0.6, ['frostbite']):
                self.dmg_make('s2', 10.52)
        else:
            self.dmg_make('s2', 2.08)
            self.afflics.frostbite('s2',120,0.287,duration=30)
            self.dmg_make('s2', 6.24)
            self.dragonform.charge_gauge(530, utp=True)
            self.inspiration.add(2)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)