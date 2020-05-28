from core.advbase import *
from slot.a.all import *
from slot.d.flame import *

def module():
    return Aurien

class Aurien(Adv):
    comment = 'no s1'
    a1 = ('s',0.4,'hp70')

    conf = {}
    conf['slots.a'] = Primal_Crisis()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s2, x=5
    """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Marth', 'Tiki']

    def s2_proc(self, e):
        self.afflics.burn(e.name,100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)