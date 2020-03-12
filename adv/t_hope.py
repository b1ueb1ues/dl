from core.simulate import test_with_argv
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Templar_Hope

class Templar_Hope(Adv):
    conf = {}
    conf['slot.a'] = Valiant_Crown()+Beautiful_Nothingness()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, x=2
        """
    
    def s1_proc(self, e):
        Teambuff('s1', 0.25, 15, 'defense').on()

if __name__ == '__main__':
    test_with_argv('t_hope', *sys.argv)