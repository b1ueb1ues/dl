from core.advbase import *
from module.bleed import Bleed

def module():
    return Addis

class Addis(Adv):
    comment = 's2 c2 s1 c5fsf c4fs s1; hold s2s1 until bleed under 3'

    a3 = ('bk',0.20)
    conf = {}
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s2, s1.charged>=s1.sp-260 and seq=5 and self.bleed._static['stacks'] != 3
        `s1, s2.charged<s2.sp and self.bleed._static['stacks'] != 3
        `fs, self.s2buff.get() and seq=4 and self.s1.charged>=s1.sp-200
        """
    coab = ['Akasha','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def getbleedpunisher(self):
        if self.bleed._static['stacks'] > 0:
            return 0.08
        return 0

    def prerun(self):
        random.seed()
        self.s2buff = Selfbuff('s2_shapshifts1',1, 10,'ss','ss')
        self.s2str = Selfbuff('s2_str',0.25,10)
        self.bleedpunisher = Modifier('bleed','att','killer',0.08)
        self.bleedpunisher.get = self.getbleedpunisher
        self.bleed = Bleed('g_bleed',0).reset()
        #self.crit_mod = self.rand_crit_mod

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s2buff = Dummy()

    def s1_proc(self, e):
        if self.s2buff.get():
            self.s2buff.buff_end_timer.timing += 2.5
            self.s2str.buff_end_timer.timing += 2.5
            if random.random() < 0.8:
                Bleed(e.name, 1.32).on()
        else:
            self.afflics.poison(e.name,100,0.53)


    def s2_proc(self, e):
        self.s2buff.on()
        self.s2str.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)