from core.advbase import *
from slot.a import *
from slot.d import *
import adv.audric

def module():
    return Audric

class Audric(adv.audric.Audric):
    a1 = ('dp', 10)
    
    conf = adv.audric.Audric.conf.copy()
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=3
    """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)