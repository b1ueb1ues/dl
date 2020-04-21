from core.advbase import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)
    conf = {}
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `fs, x=3
        """
    coab = ['Ieyasu','Wand','Dagger']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)