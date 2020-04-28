from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Ranzal

class Ranzal(Adv):
    comment = 'do not use fs'

    conf = {}
    conf['slots.a'] = Kung_Fu_Masters()+United_by_One_Vision()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1 
        """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)