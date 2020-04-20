from core.advbase import *

def module():
    return Kleimann

class Kleimann(Adv):
    a1 = ('fs',0.4)
    a3 = ('s',0.2)
 
    conf = {}
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        """
    coab = ['Ieyasu','Bow','Dagger']
    

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)