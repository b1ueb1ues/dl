from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import X_alt
import wep.wand

def module():
    return Lily

cp_auto_conf = wep.wand.conf.copy()
cp_auto_conf.update({
    'x1.dmg': 1.27075,
    'x2.dmg': 1.3685,
    'x3.dmg': 1.38,
    'x4.dmg': 1.8975,
    'x5.dmg': 2.599,
})

# C1: 1x 127.075%
# C2: 136.85%
# C3: 3x 46%
# C4: 2x 94.875%
# C5: 1x 75.9% + 4x 46%
75.9+46*4

class Lily(Adv):    
    a1 = ('a',0.20,'hp100')
    a3 = [('prep',1.00), ('scharge_all', 0.05)]

    conf = {}
    
    comment = 's1 for freeze/frostbite only'
    conf['slots.a'] = Candy_Couriers()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end'), cancel
        `s1, not self.sim_afflict
        `s3
        `s4
        `s2
    """
    coab = ['Blade', 'Renee', 'Tiki']
    share = ['Gala_Elisanne', 'Eugene']

    # conf['slots.a'] = Candy_Couriers()+His_Clever_Brother()
    # conf['slots.d'] = Siren()
    # conf['acl'] = """
    #     `dragon.act('c3 s end'), cancel
    #     `s3
    #     `s4
    #     `s2
    #     `s1
    # """
    # coab = ['Blade', 'Dagger', 'Lazry']
    # share = ['Ranzal', 'Eugene']

    def prerun(self):
        self.crystalian_princess = X_alt(self, 'crystalian_princess', cp_auto_conf, x_proc=self.l_cp_x)

    def l_cp_x(self, e):
        with KillerModifier('alt_x_killer', 'hit', 0.3, ['frostbite']):
            self.crystalian_princess.x_proc_default(e)

    def s1_proc(self, e):
        self.afflics.freeze(e.name, 200)
        self.afflics.frostbite(e.name, 120,0.41)

    def s2_proc(self, e):
        self.crystalian_princess.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)