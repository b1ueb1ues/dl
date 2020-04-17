from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Joe

class Joe(Adv):
    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.a'] = Mega_Friends()+Dear_Diary()
    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=1
        """
    conf['afflict_res.burn'] = 0
    a1 = ('edge_burn', 70, 'hp100')

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)
        
    def s2_proc(self, e):
        self.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)