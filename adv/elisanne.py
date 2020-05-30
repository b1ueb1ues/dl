from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = 'no s2 or s3'
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.a'] = Beach_Battle()+Castle_Cheer_Corps()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `s1
        `s4
        `fs, x=5
    """
    coab = ['Tobias', 'Renee', 'Bow']
    share = ['Gala_Elisanne']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
