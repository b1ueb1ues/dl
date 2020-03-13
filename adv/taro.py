from core.advbase import *

def module():
    return Taro

class Taro(Adv):
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)