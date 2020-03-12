from core.advbase import *
from slot.a import *

def module():
    return Erik

class Erik(Adv):
    comment =''
    a1 = ('fs',0.30)
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
    """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)