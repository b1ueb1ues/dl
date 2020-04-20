from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Cassandra

class Cassandra(Adv):
    a3 = [('prep',1.00), ('scharge_all', 0.05)]
    a3 = ('ro', 0.15)

    conf = {}
    conf['slots.a'] = Candy_Couriers()+The_Plaguebringer()
    conf['slots.poison.a'] = conf['slots.a']
    conf['slots.d'] = Fatalis()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
    """
    coab = ['Curran','Berserker','Delphi']
    conf['afflict_res.poison'] = 0

    def prerun(self):
        self.hp = 80

    def s1_proc(self, e):
        self.afflics.poison('s1',120,0.582)

    def s2_proc(self, e):
        with CrisisModifier('s2', 1, self.hp):
            self.dmg_make('s2',9.72)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)