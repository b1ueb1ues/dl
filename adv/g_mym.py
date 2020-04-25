from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Gala_Mym

class Gala_Mym(Adv):
    a3 = ('dt', 0.20)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Red_Impulse()
    conf['slots.d'] = Gala_Mars()
    conf['acl'] = """
        if s
        `dragon.act('c3 s end'), self.dragonform.shift_count<1
        `dragon
        end
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Yuya']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Blade', 'Verica', 'Yuya']
    
    conf['dragonform1'] = {
        'act': 'c3 s',

        'dx1.dmg': 2.16,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.38,
        'dx2.startup': 48 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.03,
        'dx3.startup': 42 / 60.0, # c3 frames
        'dx3.recovery': 86 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 7.56,
        'ds.recovery': 142 / 60, # skill frames
        'ds.hit': 2,
    }
    conf['dragonform2'] = {
        'dx1.dmg': 2.32,
        'dx1.startup': 16 / 60.0, # c1 frames

        'dx2.dmg': 2.56,
        'dx2.startup': 44 / 60.0, # c2 frames

        'dx3.dmg': 3.25,
        'dx3.startup': 36 / 60.0, # c3 frames
        'dx3.recovery': 84 / 60.0, # recovery

        'ds.dmg': 11.62,
        'ds.recovery': 125 / 60, # skill frames
    }
    conf['dragonform'] = conf['dragonform1']

    def ds_proc(self):
        return self.dmg_make('ds',self.dragonform.conf.ds.dmg,'s')

    def prerun(self):
        self.a1_buff = Selfbuff('flamewyrm', 0.15, -1, 'att', 'passive')
        Event('dragon').listener(self.a1_on)

    def a1_on(self, e):
        if not self.a1_buff.get():
            self.a1_buff.on()
        else:
            self.dragonform.conf += self.conf.dragonform2

    def s1_proc(self, e):
        self.dragonform.charge_gauge(5)

    def s2_proc(self, e):
        if self.a1_buff.get():
            self.dmg_make('o_s2_boost', 4.16)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)