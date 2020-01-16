if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy


def module():
    return Noelle

class Noelle(Adv):
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()

    conf['acl'] = """
        `# fs_sp = this.ceiling(this.float_problem(this.conf.fs.sp*this.float_problem(this.sp_mod('fs_missile'))))
        `s1
        `fs, this.fs_prep_c==3 and s1.charged>=s1.sp*1/2-fs_sp
        `fs, this.fs_prep_c==1 and s1.charged>=s1.sp*3/4-fs_sp
        `s2, seq=5 and cancel
        """

    def init(this):
        energy.Energy(this,{},{})
        this.a1_iscding = 0
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s1',0.25,15).on()

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')

    def a1_act(this):
        #logcat()
        #print this.a1_iscding
        #exit()
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.0,10,'def').on()
            #Teambuff('db_test',0.10,15).on()
            Event('defchain')()
        else:
            log('cd','a1','trigger failed')

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()
        return r


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

