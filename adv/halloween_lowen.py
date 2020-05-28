import adv.adv_test
from core.advbase import *
from slot.a.all import The_Bridal_Dragon, From_Whence_He_Comes
from slot.d import PopStar_Siren

def module():
    return Halloween_Lowen

class Halloween_Lowen(Adv):
    comment = 'hlowen dps <= burn DoT'
    a1 = ('fsprep', 3)
    a3 = ('prep', 0.75)

    conf = {}
    conf['slots.a'] = From_Whence_He_Comes()+The_Bridal_Dragon()
    conf['slots.burn.a'] = conf['slots.a']
    conf['slots.d'] = PopStar_Siren()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, x=5
        `s2, pin='prep' or x=5 and self.hp_stack < 3
        `fs, s=3 and self.fs_prep_c > 0
    """
    coab = ['Bow', 'Euden', 'Yuya']

    def init(self):
        self.hp_stack = 0
        # self.doublebuff = self.condition('doublebuff 3 other')
    
    def s1_proc(self, e):
        Event('defchain')()
        # if self.doublebuff:
        #     self.Teambuff('defchain',0.10,15).on()
    
    def s2_proc(self, e):
        if self.hp_stack < 3:
            self.hp_stack += 1
        log('debug', 'HP {}0%'.format(self.hp_stack))

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

