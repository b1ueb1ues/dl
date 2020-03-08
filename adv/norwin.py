import adv.adv_test
from core.advbase import *

def module():
    return Norwin

class Norwin(Adv):
    a3 = ('k_blind', 0.20)
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    conf['afflict_res.blind'] = 80

    def s1_proc(self, e):
        self.afflics.blind('s1',100)
        Teambuff('a1',0.15*self.afflics.blind.get(),10).on()


    def s2_proc(self, e):
        with Modifier("s1killer", "blind_killer", "hit", 0.44):
            self.dmg_make('s1',3*2.45)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
