from core.advbase import *
from slot.a import *

def module():
    return Summer_Celliera

class Summer_Celliera(Adv):
    a1 = ('bc',0.13)
    a3 = ('bt',0.30)
    conf = {}
    conf['slots.a'] = VC() + Memory_of_a_Friend()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['acl'] = """
        `s2
        `s1
        `s3, fsc
        `fs, seq=2
        """
    coab = ['Blade','Dagger','Summer_Estelle']
    conf['afflict_res.bog'] = 100

    def init(self):
        self.phase['s2'] = 0

    def s1_proc(self, e):
        #560+168+392
        self.dmg_make(e.name,1.84)
        self.afflics.bog.on(e.name, 110)
        self.dmg_make(e.name,5.52)

    def s2_proc(self, e):
        self.phase[e.name] += 1
        if self.phase[e.name] == 1:
            Teambuff(f'{e.name}_def',0.1,10,'defense').on()
        elif self.phase[e.name] == 2:
            Teambuff(f'{e.name}_def',0.1,10,'defense').on()
            Teambuff(e.name,0.1,10).on()
        elif self.phase[e.name] == 3:
            Teambuff(f'{e.name}_def',0.1,10,'defense').on()
            Teambuff(e.name,0.1,10).on()
            Spdbuff(f'{e.name}_spd',0.2,10,wide='team').on()
        self.phase[e.name] %= 3


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)