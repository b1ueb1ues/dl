from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Heinwald

class Heinwald(Adv):
    a1 = ('s',0.4,'hp70')
    a3 = [('prep',1.00), ('scharge_all', 0.05)]

    conf = {}
    conf['acl'] = '''
        queue prep and not self.s3_buff
        `s3;s1;s4;s2
        end
        `s4
        `s1
        `s2, cancel
        `dragon.act('c3 s end'),x=5
        '''
    coab = ['Blade','Wand','Bow']
    share = ['Curran']
    
    def s2_proc(self, e):
        self.s2_buff = Selfbuff(e.name,0.25,10).on()
        if self.condition('buff all teammates'):
            Teambuff(e.name,0.15,10).on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
