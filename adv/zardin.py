from core.advbase import *
from slot.a import *

def module():
    return Zardin

class Zardin(Adv):
    a1 = ('a',0.10,'hp100')
    
    conf = {}
    conf['slots.a'] = TSO()+Primal_Crisis()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    coab = ['Xander', 'Dagger', 'Summer_Estelle']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)