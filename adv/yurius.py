from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Yurius

class Yurius(Adv):
    a3 = ('prep', 100)
    conf = {}
    conf['slots.a'] = Primal_Crisis()+Candy_Couriers()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        if self.afflics.frostbite.get()
        `dragon, not self.dragondrive_buff.get() and (self.duration<=120 or self.dragonform.dragon_gauge>=2130 or self.dragonform.shift_count>0)
        else
        `dragon, self.dragondrive_buff.get()
        end
        queue prep and self.duration>120
        `s2; s1; s3
        end
        `s2, cancel
        `s1, cancel
        `s3, cancel
        # Bow(15%) + DDrive(35%) 
        `fs, x=5 and self.mod('sp')>=1.45
    """
    coab = ['Blade','Hunter_Sarisse','Xander']

    # conf['sim_afflict.efficiency'] = 1
    # conf['sim_afflict.type'] = 'frostbite'

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
                self.dmg_make(e.name, 7.92)
            self.dragonform.add_drive_gauge_time(self.s1.ac.getstartup()+self.s1.ac.getrecovery(), skill_pause=True)
        else:
            self.dmg_make(e.name, 7.56)
            self.dragonform.charge_gauge(530, utp=True)
            self.inspiration.add(1, team=False)

    def s2_proc(self, e):
        if self.dragondrive_buff.get():
            with KillerModifier('s2_killer', 'hit', 0.6, ['frostbite']):
                self.dmg_make(e.name, 10.52)
            self.dragonform.add_drive_gauge_time(self.s2.ac.getstartup()+self.s2.ac.getrecovery(), skill_pause=True)
        else:
            self.dmg_make(e.name, 2.08)
            self.afflics.frostbite(e.name,120,0.287,duration=30)
            self.dmg_make(e.name, 6.24)
            self.dragonform.charge_gauge(530, utp=True)
            self.inspiration.add(2, team=False)

    def s3_proc(self, e):
        if self.dragondrive_buff.get():
            self.dragonform.add_drive_gauge_time(self.s3.ac.getstartup()+self.s3.ac.getrecovery(), skill_pause=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
