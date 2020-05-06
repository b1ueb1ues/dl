from core.advbase import *

def module():
    return Taro

class Taro(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `s2
        """
    coab = ['Wand','Dagger','Tiki']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)