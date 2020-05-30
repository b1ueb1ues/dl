from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Sylas

class Sylas(Adv):
    a3 = ('a',0.15,'hp70')

    comment = 'no skill haste for team'
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, x=5
        """
    coab = ['Eleonora','Dragonyule_Xainfried','Blade']
    conf['afflict_res.poison'] = 0

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Dragonyule_Xainfried','Lin_You']

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.5, ['poison']):
            self.dmg_make(e.name, 11.04)
            self.afflics.poison(e.name,120,0.582)

    def s2_proc(self, e):
        Selfbuff(f'{e.name}_sp',0.30,15,'sp','buff').on()
        Teambuff(e.name,0.25/2,15,'att','buff').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
