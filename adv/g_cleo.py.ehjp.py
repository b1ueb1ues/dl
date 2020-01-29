import adv_test
from adv import *
import g_cleo
from slot.a import Amulet

class King_of_the_Skies(Amulet):
    att = 39

class Candy_Couriers(Amulet):
    att = 65
    a = [('s',0.40)]

def module():
    return G_Cleo

class G_Cleo(g_cleo.G_Cleo):
    comment = '4 Gleo vs EHJP; with simulated break; no team dps;'

    def d_slots(this):
        this.slots.a = Candy_Couriers()+King_of_the_Skies()
        this.slots.d = slot.d.Shinobi()
    
    def d_acl(this):
        this.conf['acl'] = """
            `rotation
        """
        this.conf['rotation'] = """
            s2 s1 c5 fs s3 c5 s1 c5 c5 fs s2 s1 c5 s3 c5 fs s1 end
        """

    def prerun(this):
        super().prerun()
        this.odbk = 991202+792960
        this.ehjp = 4488479
        this.dmgsum = 0
        this.broken_punisher = Selfbuff(name='candy_couriers', value=0.25, duration=-1, mtype='att', morder='bk')

    def dmg_proc(this, name, amount):
        this.dmgsum += int(amount) * 4
        if this.dmgsum > this.odbk and this.dmgsum-(int(amount)*4) < this.odbk:
            log('debug', 'odbk', 'BREAK start')
            this.broken_punisher.on()
            Timer(this.break_end).on(10)
        log('debug', 'ehjp', '{}/{} ({:.0%})'.format(this.dmgsum, this.ehjp, this.dmgsum/this.ehjp))
        if this.dmgsum > this.ehjp:
            log('debug', 'ehjp is kill')

    def break_end(this, t):
        log('debug', 'odbk', 'BREAK end')
        this.broken_punisher.off()

    def dmg_make(this, name, dmg_coef, dtype=None, fixed=False):
        if this.broken_punisher.get():
            generic_name = name.split('_')[0]
            if generic_name[0] == 'x':
                generic_name = 'x'
            name = 'o_'+generic_name+'_on_bk'
        if dtype == None:
            dtype = name
        count = this.dmg_formula(dtype, dmg_coef) if not fixed else dmg_coef
        log('dmg', name, count)
        this.dmg_proc(name, count)
        return count

    def dmg_formula(this, name, dmg_coef):
        att = 1.0 * this.att_mod() * this.base_att
        if this.broken_punisher.get():
            armor = 10.0 * this.def_mod() * 0.6
        else:
            armor = 10.0 * this.def_mod()
        return 5.0/3 * dmg_coef * this.dmg_mod(name) * att/armor * 1.5   # true formula 

    def s2_proc(this, e):
        super().s2_proc(e)
        Debuff('s2',0.10,20).on()
        Debuff('s2',0.10,20).on()
        Debuff('s2',0.10,20).on()

    def fs_proc(this, e):
        if this.fsa_charge:
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
        super().fs_proc(e)


if __name__ == '__main__':
    conf = {}
    adv_test.team_dps = 0
    adv_test.test(module(), conf, verbose=0)

