from core.advbase import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Victor

class Victor(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1, self.bleed._static['stacks'] < 3
        `s2, x=5
        """
    coab = ['Akasha','Dragonyule_Xainfried','Lin_You']

    def prerun(self):
        random.seed()
        self.bleed = Bleed('g_bleed',0).reset()

    def s1_proc(self, e):
        if random.random() < 0.8:
            Bleed(e.name, 1.46).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
