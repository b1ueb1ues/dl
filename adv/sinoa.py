import adv.adv_test
from core.advbase import *
from core.advbase import *

def module():
    return Sinoa

class Sinoa(Adv):
    a1 = ('a',0.13,'hp100')
    a3 = ('bt',0.2)
    conf = {}
    conf['slot.d'] = slot.d.Dreadking_Rathalos()
    conf['acl'] = '''
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, seq=5
        '''

    def prerun(self):
        self.s1_buff_mode = 'means'

    def s1_proc(self, e):
        if self.s1_buff_mode == 'means':
            Teambuff('s1_att',0.25/4,15,'att').on()
            Teambuff('s1_crit',0.25/4,10,'crit').on()
        elif self.s1_buff_mode == 'random':
            r = random.random()
            if r<0.25  :
                Teambuff('s1_att',0.25,15,'att').on()
            elif r<0.5 :
                Teambuff('s1_crit',0.25,10,'crit').on()
            elif r<0.75:
                Event('defchain')()
            else:
                log('debug','s1 HP buff')
        elif self.s1_buff_mode == 'att':
            adv.Teambuff('s1_att',0.25,15,'att').on()
        elif self.s1_buff_mode == 'crit':
            adv.Teambuff('s1_crit',0.25,10,'crit').on()

if __name__ == '__main__':
    conf = {}
    module().comment = ''
    adv.adv_test.test(module(), conf)


