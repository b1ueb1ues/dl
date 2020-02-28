import adv.adv_test
from core.advbase import *
from slot.a.all import The_Bridal_Dragon, From_Whence_He_Comes, Castle_Cheer_Corps
from slot.d import PopStar_Siren

def module():
    return Halloween_Lowen

class Halloween_Lowen(Adv):
    comment = 'hlowen dps <= burn DoT'
    a1 = ('fsprep', 3)
    a3 = ('prep','75%')

    conf = {}
    conf['slots.a'] = From_Whence_He_Comes()+Castle_Cheer_Corps()
    conf['slots.d'] = PopStar_Siren()
    # conf['acl'] = """
    #     `s3, not this.s3_buff
    #     `s1, x=5
    #     `s2, pin='prep' or x=5 and this.hp_stack < 3
    #     `fs, s=3 and this.fs_prep_c > 0
    # """

    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, x=5
    """


    def init(this):
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

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

