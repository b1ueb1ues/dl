import adv.adv_test
from core.advbase import *
from slot.a.all import The_Bridal_Dragon, From_Whence_He_Came
from slot.d import PopStar_Siren

def module():
    return H_Lowen

class H_Lowen(Adv):
    comment = 'hlowen dps <= burn DoT'
    a3 = ('prep','75%')

    conf = {}
    conf['slots.a'] = The_Bridal_Dragon()+From_Whence_He_Came()
    conf['slots.d'] = PopStar_Siren()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, x=5
        `s2, pin='prep' or x=5 and this.hp_stack < 3
        `fs, s=3 and this.o_fs_prep_c > 0
    """

    def init(this):
        this.o_fs_prep_c = 3
        this.hp_stack = 0
        # this.doublebuff = this.condition('doublebuff 3 other')
    
    def s1_proc(this, e):
        Event('defchain')()
        # if this.doublebuff:
        #     this.Teambuff('defchain',0.10,15).on()
    
    def s2_proc(this, e):
        if this.hp_stack < 3:
            this.hp_stack += 1
        log('debug', 'HP {}0%'.format(this.hp_stack))

    def fs_proc(this, e):
        fs_hits = {'sword': 1, 'blade': 1, 'dagger': 3, 'axe': 1, 'lance': 5, 'wand': 2, 'bow': 8, 'staff': 4}
        if this.o_fs_prep_c > 0:
            diff = this.o_fs_prep_c - max(this.o_fs_prep_c-fs_hits[this.slots.c.wt], 0)
            for _ in range(diff):
                this.charge_p('fs_charge','25%')
            this.o_fs_prep_c = this.o_fs_prep_c - diff

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf,verbose=0, mass=0)

