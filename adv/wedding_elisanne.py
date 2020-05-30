from core.advbase import *
from slot.a import *

def module():
    return Wedding_Elisanne


class Wedding_Elisanne(Adv):
    comment = '2in1'
    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+United_by_One_Vision()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1,fsc and s2.charged<s2.sp-749
        `s2
        `fs,x=2
    """
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']

    def s2_proc(self, e):
        if self.condition(f'{e.name} defdown for 10s'):
            self.s2_debuff = Debuff(e.name,0.15,10,1)
            self.s2_debuff.bufftime = self.s2_debuff._no_bufftime
            self.s2_debuff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
