import adv.adv_test
import adv
from adv import *

def module():
    return Sinoa

class Sinoa(adv.Adv):
    a1 = ('a',0.13,'hp100')
    a3 = ('bt',0.2)
   # conf = {}
   # import slot
   # conf['slots.a'] = slot.a.Bellathorna()+slot.a.RR()


    def s1_proc(this, e):
        adv.Teambuff('s1_att',0.25/4,15,'att').on()
        adv.Teambuff('s1_crit',0.25/4,10,'crit').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = '''
        `s1
        `s2
        `fs,seq=5
        '''
    adv_test.test(module(), conf, verbose=-2, mass=0)


