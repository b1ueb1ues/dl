from core.advbase import *
from slot.d import *

def module():
    return Orsem

class Orsem(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')
    
    conf = {}
    conf['slots.d'] = Nimis()
    conf['acl'] = """
        `dragon
        `s3
        `s1
        `s4
        `s2, fsc
        `fs, x=4
    """
    coab = ['Dagger2', 'Xander', 'Yurius']
    share = ['Gala_Elisanne', 'Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
