from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Melody

class Melody(Adv):
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = RR()+ADD()
    conf['slots.d'] = Ariel()
    conf['acl'] = """
        `s1
        `s3, x=4 or x=5
    """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)