import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Valerio

class Valerio(Adv):
    conf = {}
    conf['slot.a'] = Resounding_Rendition()+Beautiful_Nothingness()
    conf['slot.d'] = Siren()
    conf['acl'] = """
        `appetizer, s1.check()
        `s1
        `entree, s2.check()
        `s2, x=5
        `s3, x=5
    """
    conf['afflict_res.frostbite'] = 0

    def prerun(self):
        self.inspiration = 0
        self.stance = None
        self.stance_list = ['appetizer', 'entree', 'dessert']
        self.crit_mod = self.custom_crit_mod
        self.a1_cd = False
        self.s1_debuff = Debuff('s1', 0.05, 30)
        self.s2_buff = [
            Teambuff('s2', 0.08, 15, 'defense'),
            Teambuff('s2', 0.10, 15, 'crit', 'chance'),
            Teambuff('s2', 0.08, 15)
        ]

    def custom_crit_mod(self):
        crit = self.rand_crit_mod()
        if crit > 1 and not self.a1_cd:
            # Increases attack rate by 10% for 20 seconds each
            # time one of the user's attacks is a critical hit.
            # After activating, this ability will not activate again
            # for 10 seconds.
            # can it stack?
            Spdbuff('a1', 0.10, 20).on()
            self.a1_cd = True
            Timer(self.a1_cd_off).on(10)
        return crit

    def a1_cd_off(self, t):
        self.a1_cd = False

    def change_stance(self, stance):
        if self.hits > 20:
            if isinstance(stance, int) and stance != self.stance and -1 < stance < 3:
                self.stance = stance
                log('debug', 'stance', self.stance_list[self.stance])
                return True
            elif stance in self.stance_list and stance != self.stance_list[self.stance]:
                self.stance = self.stance_list.index(stance)
                log('debug', 'stance', self.stance_list[self.stance])
                return True
        return False

    def appetizer(self):
        return self.change_stance(0)

    def entree(self):
        return self.change_stance(1)
    
    def dessert(self):
        return self.change_stance(2)

    def s1_proc(self, e):
        # Deals water damage to enemies directly ahead,
        # and applies one of the following effects based
        # on the user's current cooking stance:
        if self.stance == 0:
            # Appetizer Stance: Inflicts frostbite and
            # reduces enemies' defense by 5% for 30 seconds.
            # This defense reduction effect will not stack.
            self.afflics.frostbite('s1',120,1.00)
            self.s1_debuff.on()
        else:
            pass
            # Entrée Stance: Inflicts stun and
            # reduces enemies' strength by 15% for 30 seconds.
            # This strength reduction effect will not stack.
            
            # Dessert Stance: Inflicts freeze.


    def s2_proc(self, e):
        # Applies one of the following effects to the entire team
        # based on the user's current cooking stance:

        if self.stance == 0:
            # Appetizer Stance: Increases defense by 15% for
            # 15 seconds, and inspiration by two stages.
            # This defense increase will not stack.
            self.inspiration += 2
            self.s2_buff[0].on()
        elif self.stance == 1:
            # Entrée Stance: Increases critical rate by 10% for
            # 15 seconds, and inspiration by three stages.
            # This critical rate increase will not stack.
            self.inspiration += 3
            self.s2_buff[1].on()
        elif self.stance == 2:
            # Dessert Stance: Increases strength by 8% for
            # 15 seconds, and inspiration by two stages.
            # This strength increase will not stack.
            self.inspiration += 2
            self.s2_buff[2].on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

