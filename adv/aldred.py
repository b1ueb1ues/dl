from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Aldred

class Aldred(Adv):
    comment = 'maintain dragondrive'

    conf = {}
    conf['slots.a'] = Heralds_of_Hinomoto()+Dear_Diary()
    conf['slots.d'] = Fatalis()
    conf['slots.poison.a'] = Heralds_of_Hinomoto()+The_Plaguebringer()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2
        `dragon, not self.dragondrive_buff.get()
        `s1, x=5
    """
    coab = ['Wand','Berserker','Curran']

    def prerun(self):
        self.dragondrive_buff = Selfbuff('dragondrive', 0.30, -1, 's', 'passive')
        self.dragonform.set_dragondrive(self.dragondrive_buff)

        self.a3_str = Modifier('a3', 'att', 'passive', 0.20)
        self.s2_str = Selfbuff('s2', 0.20, -1, 'att', 'buff') # doesnt proc doublebuff reeeee
        self.s2_tick = Timer(self.s2_degen, 2.9, 1)
        self.s2_stuff_timer = Timer(self.s2_stuff_off)
        self.s2_on = False

        self.conf.x1.utp = 120
        self.conf.x2.utp = 120
        self.conf.x3.utp = 120
        self.conf.x4.utp = 180
        self.conf.x5.utp = 180

    def d_slots(self):
        if self.duration <= 60:
            self.conf['slots.a'] = The_Chocolatiers()+TL()
            self.conf['slots.poison.a'] = The_Chocolatiers()+The_Plaguebringer()

    def x_proc(self, e):
        if self.dragondrive_buff.get():
            try:
                utp = self.conf[e.name].utp
                self.dragonform.charge_gauge(utp, utp=True)
            except:
                pass

    def s1_proc(self, e):
        if self.dragondrive_buff.get():
            self.dmg_make(e.name, 2.42*3)
            with CrisisModifier(e.name, 1.00, self.hp):
                self.dmg_make(e.name, 2.42)
            self.dragonform.add_drive_gauge_time(self.s1.ac.getstartup()+self.s1.ac.getrecovery(), skill_pause=True)
            self.dragonform.charge_gauge(-750, utp=True)
            self.s1.charge(self.sp_convert(0.50, self.conf.s1.sp))
        else:
            self.dmg_make(e.name, 2.42*4)
        # 242 * 4 mod, 4 hits, 2.4s
        # 242 * 4 w/ 2x crisis
        # -750 dd points
        # +50% skill gauge
        # 2.1666667461395264

    def s2_proc(self, e):
        if self.dragondrive_buff.get():
            self.s2_stuff_on()
            self.s2_stuff_timer.on(40 * self.mod('bt'))
            self.dragonform.add_drive_gauge_time(self.s2.ac.getstartup()+self.s2.ac.getrecovery(), skill_pause=True)
            self.dragonform.charge_gauge(3000, utp=True)
        else:
            self.dragonform.charge_gauge(1200, utp=True)
            # 1 hp loss = 1 gauge gain, will assume 3000 max hp here
            if self.hp > 30:
                self.dragonform.charge_gauge(3000 * (self.hp-30)/100, utp=True)
                self.set_hp(30)
        # +1200 dd points
        # 1.3333333730697632s

    def s2_stuff_on(self):
        self.a3_str.on()
        self.s2_str.on()
        self.s2_tick.on()

    def s2_stuff_off(self, t):
        self.a3_str.off()
        self.s2_str.off()
        self.s2_tick.off()

    def s2_degen(self, t):
        if self.hp > 0:
            self.set_hp(self.hp-6)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)