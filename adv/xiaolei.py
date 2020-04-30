from core.advbase import *

def module():
    return Xiao_Lei

class Xiao_Lei(Adv):
    a1 = ('s',0.2)
    
    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3
        """
    coab = ['Blade','Dagger','Peony']

    def s2_proc(self, e):
        Teambuff('s2cc',0.08,10,'crit','rate').on()
        Teambuff('s2cd',0.40,10,'crit','dmg').on()



if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)