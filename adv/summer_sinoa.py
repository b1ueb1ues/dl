from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Summer_Sinoa

class Summer_Sinoa(Adv):
    a1 = ('s', 0.30)
    conf = {}
    conf['slots.d'] = Ariel()
    conf['slots.a'] = Candy_Couriers()+The_Fires_of_Hate()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s4
        `s2, self.overload=3
        `s1
        """
    coab = ['Blade','Eleonora','Tobias']
    share = ['Curran']

    def prerun(self):
        self.overload = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        self.overload = -1

    def charge(self, name, sp):
        # sp should be integer
        sp_overload = self.sp_convert(self.sp_mod(name)-self.overload*0.30, sp)
        sp = self.sp_convert(self.sp_mod(name), sp)
        for s in self.skills:
            if s == self.s1:
                s.charge(sp_overload)
            else:
                s.charge(sp)
        self.think_pin('sp')
        log('sp', name, sp, ', '.join([f'{s.charged}/{s.sp}' for s in self.skills]))

    def s1_before(self, e):
        if self.overload == -1:
            return
        if self.overload < 3:
            self.overload += 1
        self.determination = Selfbuff('determination', 0.15+0.05*self.overload, -1, 's', 'passive').on()

    def s1_proc(self, e):
        self.afflics.poison(e.name, 120, 0.582)
        if self.overload == -1:
            return
        self.determination.off()

    def s2_proc(self, e):
        if self.overload == 3:
            self.inspiration.add(2, team=True)
            Teambuff('s2_crit_rate', 0.20, 30, 'crit', 'rate').on()
            Teambuff('s2_crit_dmg', 0.15, 30, 'crit', 'damage').on()
        else:
            buffs = [
                lambda: self.inspiration.add(2),
                lambda: Selfbuff('s2_crit_rate', 0.15, 30, 'crit', 'rate').on(),
                lambda: Selfbuff('s2_crit_dmg', 0.15, 30, 'crit', 'damage').on(),
            ]
            log('debug', 'overload', self.overload)
            for _ in range(max(1, self.overload)):
                buff = random.choice(buffs)
                buff()
                buffs.remove(buff)
        self.overload = 0

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
