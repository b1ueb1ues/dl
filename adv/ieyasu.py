from core.advbase import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(Adv):
    a1 = ('cc',0.13,'hp70')
    a2 = ('cd',0.3)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+United_by_One_Vision()
    conf['acl'] = """
        ##Use Gala Cat Sith only when out of Skillful Trickery
        #`dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s1, self.s3_buff
        `s2, x=5
        `s4, fsc
        `fs, x=5 and self.s3_buff
    """
    coab = ['Wand','Dagger','Axe2']
    share = ['Curran']

    def s2ifbleed(self):
        if self.bleed._static['stacks'] > 0:
            return self.s2buff.get()
        return 0

    def prerun(self):
        self.s2buff = Selfbuff('s2',0.20,15,'crit')
        self.s2buff.modifier.get = self.s2ifbleed
        self.bleed = Bleed('g_bleed',0).reset()
        self.s2charge = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.bleed = Bleed('g_bleed',0).reset()

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.2, ['poison']):
            self.dmg_make(e.name, 12.40)
            Bleed(e.name, 1.46).on()

    def s2_proc(self, e):
        self.s2buff.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)