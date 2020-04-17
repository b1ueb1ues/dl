from core.advbase import *
import slot
from slot.d import *

def module():
    return Student_Maribelle

class Student_Maribelle(Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('bk',0.3)
    conf = {}
    conf['slots.d'] = Sakuya()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
    """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)