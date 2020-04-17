from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Templar_Hope

class Templar_Hope(Adv):
    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+Beautiful_Nothingness()
    conf['slots.d'] = AC011_Garland
    conf['acl'] = """
        `dragon
        `s2
        `s3
        `fs, x=2
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    
    def s1_proc(self, e):
        Teambuff('s1', 0.25, 15, 'defense').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)