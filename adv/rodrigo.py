from core.advbase import *
from slot.a import *

def module():
    return Rodrigo

class Rodrigo(Adv):
    a1 = ('a',0.15,'hp70')
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=3
        """
    coab = ['Ieyasu','Wand','Forte']

    def s1_proc(self, e):
        self.afflics.poison(e.name,120,0.582)

    def s2_proc(self, e):
        self.afflics.poison(e.name,120,0.582)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)