from core.advbase import *
from slot.a import *

def module():
    return Louise

class Louise(Adv):
    a1 = ('od',0.13)
    comment = 'no fs'
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def s1_proc(self, e):
        self.afflics.poison(e.name, 120, 0.582)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 8.07)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)