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
    a3 = ('primed_def',0.08)

    conf = {}
    conf['slots.d'] = Freyja()
    conf['slots.a'] = A_Dogs_Day()+Castle_Cheer_Corps()

    conf['acl'] = """
        `# fs_sp = this.ceiling(this.float_problem(this.conf.fs.sp*this.float_problem(this.sp_mod('fs_missile'))))
        `s1
        `fs, this.fs_prep_c==3 and s1.charged>=s1.sp*1/2-fs_sp
        `fs, this.fs_prep_c==1 and s1.charged>=s1.sp*3/4-fs_sp
        `s2, x=5
        `s3, x=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s1',0.25,15).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

