from core.advbase import *
from slot.d import *

def module():
    return Xania

class Xania(Adv):
    a1 = ('s',0.35)

    conf = {}
    conf['slots.d'] = Apollo()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2
    """
    coab = ['Blade', 'Marth', 'Joe']
    conf['afflict_res.burn'] = 0

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Marth',"Gala_Sarisse"]

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)

    def s2_proc(self, e):
        self.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)