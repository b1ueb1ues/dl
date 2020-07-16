from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Mikoto

fs_my_dude = {
    'fs.dmg': 0.0,
    'fs.sp': 0,
    'fs.charge': 0.5,
    'fs.startup': 0.2333, 
    'fs.recovery': 0.033367, 
    'fs.hit': 0,

    'x1fs.charge': 32 / 60.0, # 2 delay + fs
    'x2fs.charge': 37 / 60.0, # 7 delay + fs

    'fsf.charge': 0.5
}

class Summer_Mikoto(Adv):
    a3 = [('cc_paralysis',0.20), ('cd_paralysis',0.15)]

    conf = fs_my_dude.copy()
    conf['slots.a'] = Resounding_Rendition()+Spirit_of_the_Season()
    conf['acl'] = """
        `dragon, s=1
        `s2
        `s1
        `s3, cancel
        `s4, cancel
        `fs, self.light=self.sun and not self.illuminating_sun.get()
        `fs, self.light=self.wave and not self.celestial_wave.get()
    """
    coab = ['Blade', 'Sharena', 'Peony']
    share = ['Ranzal']
    conf['afflict_res.paralysis'] = 0

    def prerun(self):
        self.sun = Selfbuff('sun', 1, -1, 'sunlight')
        self.wave = Selfbuff('wave', 1, -1, 'wavelight')
        self.light = self.sun.on()
        self.illuminating_sun = Selfbuff('illuminating_sun', 1, -1, 'sunlight')
        self.celestial_wave = Selfbuff('celestial_wave', 1, -1, 'wavelight')
        Timer(self.light_switch, 12, True).on()

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.sun_and_wave = dummy_function

    def light_switch(self, t):
        if self.light == self.sun:
            self.sun.off()
            self.wave.on()
            self.light = self.wave
        else:
            self.sun.on()
            self.wave.off()
            self.light = self.sun

    def sun_and_wave(self):
        return self.illuminating_sun.get() and self.celestial_wave.get()

    def fs_proc(self, e):
        if self.light == self.sun:
            self.illuminating_sun.on()
        else:
            self.celestial_wave.on()

    def s1_proc(self, e):
        if self.sun_and_wave():
            # 7.690000057220459 + 17.940000534057617 * 1.3
            with KillerModifier('s1_killer', 'hit', 0.3, ['paralysis']):
                self.dmg_make(e.name, 7.60)
                self.afflics.paralysis(e.name,120, 0.97)
                self.dmg_make(e.name, 17.94)
                self.illuminating_sun.off()
                self.celestial_wave.off()
            pass
        else:
            self.dmg_make(e.name, 4.27)
            self.afflics.paralysis(e.name,120, 0.97)
            self.dmg_make(e.name, 9.97)

    def s2_proc(self, e):
        Selfbuff(e.name, 0.20, 30).on()
        if self.sun_and_wave():
            Selfbuff(f'{e.name}_crit_chance', 0.20, 30, 'crit', 'chance').on()
            Selfbuff(f'{e.name}_crit_damage', 0.15, 30, 'crit', 'damage').on()
            self.illuminating_sun.off()
            self.celestial_wave.off()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)