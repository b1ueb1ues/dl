from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Durant

class Durant(Adv):
    a1 = ('a',0.13,'hp100')
    a3 = ('cd',0.17,'hp100')

    conf = {}
    conf['slot.a'] = Proper_Maintenance()+Howling_to_the_Heavens()

    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, x=5
        """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)