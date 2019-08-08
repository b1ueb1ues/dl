import adv.adv_test
import adv
from adv import *
from module import energy

def module():
    return Yaten

class Yaten(adv.Adv):
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun
            this.conf['acl'] = """
                `s1
                `s2, fsc and this.energy() < 4
                `fs, seq=3
                """
        else:
            this.conf['acl'] = """
                `s1
                `fs, seq=3
                """

    def prerun(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()

    def c_prerun(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'s2':2} ,
                team={'s2':2}
                )
        Event('energized').listener(this.energy_doublebuff)
        this.a1atk = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        this.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()


    def a1change(this, t):
        this.a1atk.off()
        this.a1crit.off()
        if this.energy() == 5:
            this.a1atk.set(0.20)
            this.a1crit.set(0.08)
        elif this.energy() == 4:
            this.a1atk.set(0.10)
            this.a1crit.set(0.04)
        elif this.energy() == 3:
            this.a1atk.set(0.08)
            this.a1crit.set(0.03)
        elif this.energy() == 2:
            this.a1atk.set(0.06)
            this.a1crit.set(0.02)
        elif this.energy() == 1:
            this.a1atk.set(0.04)
            this.a1crit.set(0.01)
        elif this.energy() == 0:
            this.a1atk.set(0)
            this.a1crit.set(0)
        this.a1atk.on()
        this.a1crit.on()


    def s1_proc(this, e):
        if this.energy() == 5:
            energy_boost = this.energy.get_energy_boost()
            this.dmg_make('o_s1_boost',6*0.69)
            this.dmg_make('o_s1_boost_energized',6*0.69*energy_boost)
        Timer(this.a1change).on()

    def s2_proc(this, e):
        Timer(this.a1change).on()


    def energy_doublebuff(this, e):
        Selfbuff("double_buff", 0.2, 15).on()

    def s3_proc(this, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    from slot.a import *
    from slot.d import *
    conf['slot.a'] = The_Shining_Overlord()+LC()

    #conf['slot.a'] = HoH()+JotS()
    #conf['slot.a'] = The_Shining_Overlord()+ The_Petal_Queen()
    #conf['slot.a'] = The_Shining_Overlord()+ Halidom_Grooms()
    #conf['slot.d'] = Marishiten()
     
    adv_test.test(module(), conf, verbose=-2)


