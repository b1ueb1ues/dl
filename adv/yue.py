from core.advbase import *
from slot.a import *

def module():
    return Yue

class Yue(Adv):
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Breakfast_at_Valerios()
    conf['slots.burn.a'] = Kung_Fu_Masters()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1
        `s2, x=4
        `s4, x=4
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Halloween_Mym']
    share = ['Ranzal']

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Marth','Dagger2']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
