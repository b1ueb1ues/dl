from core.advbase import *
import slot

def module():
    return Kleimann

class Kleimann(Adv):
    a1 = ('fs',0.4)
    a3 = ('s',0.2)
 
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, (s1.charged>=s1.sp-self.sp_val('fs')) or (s2.charged>=s2.sp-self.sp_val('fs'))
        """


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)