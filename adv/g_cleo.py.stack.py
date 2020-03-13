from core.advbase import *
import adv.g_cleo

def module():
    return Gala_Cleo

class Gala_Cleo(adv.g_cleo.Gala_Cleo):
    def prerun(self):
        super().prerun()
        self.a1_zones = []
        self.gleo_count = 4
        self.wide = 'self'
        self.comment = '{} GCleo'.format(self.gleo_count)

    def fs_proc_alt(self, e):
        if self.a1_buffed:
            while len(self.a1_zones) > 0 and not self.a1_zones[0].get():
                self.a1_zones.pop(0)
            for _ in range(self.gleo_count):
                if self.wide == 'team':
                    buff = Teambuff('a1_str',0.25,10)
                else:
                    buff = Selfbuff('a1_str',0.25,10)
                buff.bufftime = buff.nobufftime
                self.a1_zones.append(buff)
                if len(self.a1_zones) > 4:
                    self.a1_zones.pop(0).off()
                buff.on()

    def s2_proc(self, e):
        for _ in range(self.gleo_count):
            if self.wide == 'team':
                Debuff('s2', 0.10, 20).on()
            else:
                Selfbuff('s2', -0.10, 20, mtype='def').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Gala_Cleo, *sys.argv)