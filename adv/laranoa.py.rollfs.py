import adv_test
from adv import *
from slot.a import *

def module():
    return Laranoa

class Laranoa(Adv):
    comment = 'doesn\'t count spbuff for teammates'

    a3 = ('s',0.3)
    
    def init(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
        if this.condition('never lose comboes'):
            this.dmg_proc = this.c_dmg_proc

        this.conf['slot.a'] = FB()+SS()
        if this.condition('rollfs'):
            this.conf['acl'] = """
                `s3,s1.charged>=s1.sp
                `s1,fsc
                `s2,fsc
                `dodge, fsc
                `fs
                """
        else:
            this.conf['acl'] = """
                `s3,s1.charged>=s1.sp
                `s1
                `s2
                """


    def prerun(this):
        this.hits = 0

    
    def c_s2_proc(this, e):
        Teambuff('s2_str',0.10,10).on()
        Selfbuff('s2_sp',0.20,10,'sp','passive').on()

    def s2_proc(this, e):
        Selfbuff('s2_str',0.10,10).on()
        Selfbuff('s2_sp',0.20,10,'sp','passive').on()

    def c_dmg_proc(this, name, amount):
        if name[:2] == 'x1':
            this.hits += 3
        elif name[:2] == 'x2':
            this.hits += 2
        elif name[:2] == 'x3':
            this.hits += 3
        elif name[:2] == 'x4':
            this.hits += 2
        elif name[:2] == 'x5':
            this.hits += 5
        elif name[:2] == 'fs':
            this.hits += 8
        elif name[:2] == 's1':
            this.hits += 14
        if this.hits >= 20:
            this.hits -= 20
            Selfbuff('sylvan critdmg',0.10,20,'crit','damage').on()



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)


