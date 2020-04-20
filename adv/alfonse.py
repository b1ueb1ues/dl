from core.advbase import *

def module():
    return Alfonse

class Alfonse(Adv):
    a1 = ('lo',0.50*10.0/15.0)
    a3 = ('sp',0.08)

    conf = {}
    conf['acl'] = """
        `dragon, fsc
        `s1
        `s2,fsc
        `s3,fsc
        `fs, seq=3
        """
    coab = ['Blade','Dagger','Halloween_Elisanne']
    
    def s1_before(self, e):
        Selfbuff('s1buff',0.15,10).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)