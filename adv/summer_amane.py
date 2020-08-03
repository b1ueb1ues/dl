from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Amane

class Summer_Amane(Adv):
    comment = 'no s1'
    conf = {}
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s2
        `s3
        `s4
        """
    coab = ['Blade', 'Dragonyule_Xainfried', 'Lin_You']
    share = ['Ranzal', 'Curran']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
