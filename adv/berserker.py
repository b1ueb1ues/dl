from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Dear_Diary()
    conf['slots.poison.a'] = The_Shining_Overlord()+The_Plaguebringer()
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        if self.slots.d.name != 'Fatalis'
        `dragon.act("c3 s end")
        end
        `s3, not self.s3_buff
        `s1
        `fs, x=3
        """
    coab = ['Ieyasu','Wand','Dagger']

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+JotS()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)