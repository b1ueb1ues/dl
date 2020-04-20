from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Heinwald

class Heinwald(Adv):
    a1 = ('s',0.4,'hp70')
    a3 = [('prep',1.00), ('scharge_all', 0.05)]

    conf = {}
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2, s=3 or cancel
        `s1, cancel
        """
    coab = ['Blade','Wand','Dagger']
    
    def init(self):
        if self.condition("buff all teammates"):
            self.s2_proc = self.c_s2_proc

    def prerun(self):
        self.s2ssbuff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')
        
    def c_s2_proc(self, e):
        self.s2ssbuff.on()
        Teambuff('s2team',0.15,10).on()
        Selfbuff('s2self',0.10,10).on()

    def s2_proc(self, e):
        self.s2ssbuff.on()
        Selfbuff('s2',0.25,10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)