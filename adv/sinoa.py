from core.advbase import *
from slot.a import *

def module():
    return Sinoa

class Sinoa(Adv):
    a1 = ('a',0.13,'hp100')
    a3 = ('bt',0.2)

    conf = {}
    conf['acl'] = '''
        `dragon, s=1
        `s3, not self.s3_buff
        `s1
        `s2
    '''
    coab = ['Tiki', 'Gala_Sarisse', 'Marth']

    def prerun(self):
        self.s1_buff_mode = 'means'

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.s1_buff_mode = 'means'

    def s1_proc(self, e):
        if self.s1_buff_mode == 'means':
            Teambuff(f'{e.name}_att',0.25/4,15,'att').on()
            Teambuff(f'{e.name}_crit',0.25/4,10,'crit').on()
        elif self.s1_buff_mode == 'random':
            r = random.random()
            if r<0.25  :
                Teambuff(f'{e.name}_att',0.25,15,'att').on()
            elif r<0.5 :
                Teambuff(f'{e.name}_crit',0.25,10,'crit').on()
            elif r<0.75:
                Event('defchain')()
            else:
                log('debug','s1 HP buff')
        elif self.s1_buff_mode == 'att':
            Teambuff(f'{e.name}_att',0.25,15,'att').on()
        elif self.s1_buff_mode == 'crit':
            Teambuff(f'{e.name}_crit',0.25,10,'crit').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
