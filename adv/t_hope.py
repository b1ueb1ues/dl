from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Templar_Hope

class Templar_Hope(Adv):
    conf = {}
    conf['slot.a'] = Resounding_Rendition()+Brothers_in_Arms()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, x=2
        """
    
    def s1_proc(self, e):
        Teambuff('s1', 0.25, 15, 'defense').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)