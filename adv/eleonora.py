from core.advbase import *
from slot.a import *

def module():
    return Eleonora

class Eleonora(Adv):
    a3 = ('prep','50%')
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, seq=4
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0
    a1 = ('edge_poison', 50, 'hp100')

    def s1_proc(self, e):
        self.afflics.poison(e.name,110,0.53)

    def s2_proc(self, e):
        self.afflics.poison(e.name,100,0.396)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)