from core.advbase import *

def module():
    return Malka

class Malka(Adv):
    comment = ''

    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    coab = ['Blade','Dagger','Halloween_Elisanne']

    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = RR()+JotS()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)