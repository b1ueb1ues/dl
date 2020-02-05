import adv.adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy

def module():
    return Emma

class Emma(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_att', 0.05)

    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slot.a'] = Sisters_Day_Out()+FWHC()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, cancel
        `fs, x=1
        """

    def init(this):
        comment = 'no s2'
        energy.Energy(this,{},{})
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        Teambuff('s2',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.25,15).on()

    def s2_proc(this, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

