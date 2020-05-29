from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Lazry

class Lazry(Adv):
    a1 = ('k_frostbite', 0.30)
    a3 = ('s', 0.35, 'hp70')

    conf = {}
    conf['slots.a'] = Heralds_of_Hinomoto()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        if s1.check() and self.afflics.frostbite.timeleft()<7
        `low_power
        elif s2.check()
        `low_power
        else
        `high_power
        end
        `s1
        `s2
        `fs, x=5
    """
    coab = ['Blade','Xander', 'Summer_Estelle']
    conf['afflict_res.frostbite'] = 0

    def low_power(self):
        if self.mode != 'low_power' and not self.skill._static.silence:
            log('stance', 'low_power')
            self.mode = 'low_power'
            self.s1.ac = self.a_s1
            self.s2.ac = self.a_s2
            return True
        return False

    def high_power(self):
        if self.mode != 'high_power' and not self.skill._static.silence:
            log('stance', 'high_power')
            self.mode = 'high_power'
            self.s1.ac = self.a_s1a
            self.s2.ac = self.a_s2a
            return True
        return False

    def prerun(self):
        self.mode = 'low_power'
        self.a_s1 = self.s1.ac
        self.a_s1a = S('s1', Conf({'startup': 0.10, 'recovery': 1.5667}))
        self.a_s2 = self.s2.ac
        self.a_s2a = S('s2', Conf({'startup': 0.10, 'recovery': 2.5}))
        self.a_s2a.act_event.damage = True # dude trust me:tm:
        self.s1_buff = SingleActionBuff('s1',0.20,1,'s','buff')

    def s1_proc(self, e):
        if self.mode == 'low_power':
            # 1.7699999809265137 + 1.7699999809265137 + 3.369999885559082
            # 120, 41 fb
            self.dmg_make(e.name, 1.77)
            self.afflics.frostbite(e.name,120,0.41)
            self.hits += 1
            self.dmg_make(e.name, 1.77+3.37)
            self.hits += 2
        else:
            # 1.0 + 1.0 + 1.0 + 5.730000019073486
            # 20 sd to next skill
            # 1.5666667222976685s
            self.dmg_make(f'{e.name}_high', 8.73)
            self.hits += 5
            Timer(self.s1_buff_on).on(0.001)

    def s1_buff_on(self, t):
        self.s1_buff.on()

    def s2_proc(self, e):
        if self.mode == 'low_power':
            # team 15 str 10 crit 15s
            Teambuff(e.name,0.15,15,'att','buff').on()
            Teambuff(e.name,0.10,15,'crit','chance').on()
        else:
            # 2.4700000286102295 + 9.359999656677246
            # 2.5
            # recover s1 sp
            self.dmg_make(f'{e.name}_high',11.83)
            self.hits += 2
            self.s1.charge(self.s1.sp)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)