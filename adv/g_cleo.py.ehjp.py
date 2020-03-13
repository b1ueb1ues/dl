from core.advbase import *
from module.x_alt import Fs_alt
import adv.g_cleo
from slot.a import Amulet
from slot.w.wand import Agito_Jiu_Ci

class King_of_the_Skies(Amulet):
    att = 39

class Candy_Couriers(Amulet):
    att = 65
    a = [('s',0.40)]

def module():
    return Gala_Cleo

class Gala_Cleo(adv.g_cleo.Gala_Cleo):
    conf = adv.g_cleo.Gala_Cleo.conf.copy()
    conf['slot.a'] = Candy_Couriers()+King_of_the_Skies()
    conf['slot.d'] = slot.d.Shinobi()
    conf['slot.w'] = Agito_Jiu_Ci()
    conf['acl'] = "`rotation"
    conf['rotation'] = """
        s3 s2 s1 c5 d c5 d fs s1 c5 d c5 d fs s2 s1 dragon end
    """
    comment = '4 Gleo vs EHJP; simulated break & no team dps; {}'.format(conf['rotation'].replace(' d ', ' dodge ').strip())

    def prerun(self):
        self.s1p = 0
        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :0,
            'fs.charge': 30/60.0,
            'fs.startup': 20/60.0,
            'fs.recovery': 60/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

        self.dragonform.dragon_gauge = 100
        self.dragonform.conf.act = 'c3 s c3 end'
        self.odbk = 991202+792960
        self.ehjp = 4488479
        self.dmgsum = 0
        self.broken_punisher = Selfbuff(name='candy_couriers', value=0.25, duration=-1, mtype='att', morder='bk')
        self.a1_zones = []
        for _ in range(4):
            buff = Selfbuff('a1_str',0.25,10)
            buff.bufftime = buff.nobufftime
            self.a1_zones.append(buff)

    def dmg_proc(self, name, amount):
        self.dmgsum += int(amount) * 4
        if self.dmgsum > self.odbk and self.dmgsum-(int(amount)*4) < self.odbk:
            log('debug', 'odbk', 'BREAK start')
            self.broken_punisher.on()
            Timer(self.break_end).on(10)
        log('debug', 'ehjp', '{}/{} ({:.0%})'.format(self.dmgsum, self.ehjp, self.dmgsum/self.ehjp))
        if self.dmgsum > self.ehjp:
            log('debug', 'ehjp is kill')

    def break_end(self, t):
        log('debug', 'odbk', 'BREAK end')
        self.broken_punisher.off()

    def dmg_make(self, name, dmg_coef, dtype=None, fixed=False):
        if self.broken_punisher.get():
            generic_name = name.split('_')[0]
            if generic_name[0] == 'x':
                generic_name = 'x'
            elif generic_name[0:2] == 'dx':
                generic_name = 'dx'
            name = 'o_'+generic_name+'_on_bk'
        if dtype == None:
            dtype = name
        count = self.dmg_formula(dtype, dmg_coef) if not fixed else dmg_coef
        log('dmg', name, count)
        self.dmg_proc(name, count)
        return count

    def dmg_formula(self, name, dmg_coef):
        att = 1.0 * self.att_mod() * self.base_att
        if self.broken_punisher.get():
            armor = 10.0 * self.def_mod() * 0.6
        else:
            armor = 10.0 * self.def_mod()
        return 5.0/3 * dmg_coef * self.dmg_mod(name) * att/armor * 1.5   # true formula

    def s2_proc(self, e):
        for _ in range(4):
            Selfbuff('s2', -0.10, 20, mtype='def').on()

    def fs_proc_alt(self, e):
        for buff in self.a1_zones:
            buff.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Gala_Cleo, *sys.argv)