from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lathna

class Lathna(Adv):
    comment = 'cait sith skill damage does not work on s1 extra hits'
    a1 = ('k_poison',0.15)
    a3 = ('dt', 0.25)
    
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+An_Ancient_Oath()
    conf['slots.d'] = Chthonius()
    conf['slots.poison.d'] = Gala_Cat_Sith()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s4
        `s2, x=5
        """
    coab = ['Ieyasu','Audric','Forte']
    share = ['Curran']

    def d_coabs(self):
        if self.duration <= 120 and self.duration > 60:
            self.coab = ['Ieyasu','Yaten','Dagger2']
        if self.duration <= 60:
            self.coab = ['Ieyasu','Gala_Alex','Dagger2']
        if self.sim_afflict:
            if self.duration > 120:
                self.coab = ['Ieyasu','Forte','Wand']
            if self.duration <= 120 and self.duration > 60:
                self.coab = ['Ieyasu','Forte','Dagger2']
            if self.duration <= 60:
                self.coab = ['Ieyasu','Yaten','Dagger2']
        
    conf['dragonform'] = {
        'act': 'c3 s c3 c3 c2 c2 c2',

        'dx1.dmg': 2.31,
        'dx1.startup': 19 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.54,
        'dx2.startup': 42 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.34,
        'dx3.startup': 68 / 60.0, # c3 frames
        'dx3.recovery': 72 / 60.0, # recovery
        'dx3.hit': 2,

        'ds.recovery': 124 / 60, # skill frames
        'ds.hit': 2,

        'dodge.startup': 41 / 60.0, # dodge frames
    }

    def ds_proc(self):
        dmg = self.dmg_make('ds', 3.64, 's')
        self.afflics.poison('ds',120,0.291,30,dtype='s')
        # self.afflics.poison('ds',120,3.00,30,dtype='s')
        return dmg + self.dmg_make('ds',3.64,'s')

    def prerun(self):
        self.faceless_god = Selfbuff('faceless_god',2.00,-1,'poison_killer','passive')
        Event('dragon').listener(self.a1_on)
        Event('idle').listener(self.a1_off)

        a_s1 = self.s1.ac
        a_s1a = S('s1', Conf({'startup': 0.10, 'recovery': 2.00}))
        def recovery():
            return a_s1a._recovery + a_s1.getrecovery()
        a_s1a.getrecovery = recovery
        self.s1.ac = a_s1a

    @staticmethod
    def prerun_skillshare(adv, dst):
        s = adv.__getattribute__(dst)
        a_s1 = s.ac
        a_s1a = S(dst, Conf({'startup': 0.10, 'recovery': 2.00}))
        def recovery():
            return a_s1a._recovery + a_s1.getrecovery()
        a_s1a.getrecovery = recovery
        s.ac = a_s1a

    def a1_on(self, e):
        if not self.faceless_god.get():
            self.faceless_god.on()

    def a1_off(self, e):
        if self.faceless_god.get():
            self.faceless_god.off()

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 2.37*3)
            self.dmg_make(e.name, 2.37*4*self.sub_mod('s', 'passive')*self.sub_mod('s', 'ex'), 'hecking_spaget')

            self.hits += 7

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 17.26)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)