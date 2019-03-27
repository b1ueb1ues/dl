import adv_test
import adv
from adv import *

def module():
    return Sinoa

class Sinoa(adv.Adv):
    conf = {}
    #conf['mod_wp2'] = ('buff','time',0.15)
    def pre(this):
        if this.condition('hp100'):
            this.conf['mod_a'] = ('att' , 'passive', 0.13)
        this.conf['mod_a2'] = ('buff' , 'time', 0.2)
        #this.conf['mod_wp2'] = ('buff' , 'time', 0.15)

    def s1_proc(this, e):
        r = random.random()
        if r<0.25  :
            adv.Teambuff('s1_att',0.25,15,'att').on()
        elif r<0.5 :
            adv.Teambuff('s1_crit',0.25,10,'crit').on()
        else:
            log('failed','s1')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = '''
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        '''
    adv_test.test(module(), conf, verbose=-2, mass=1)


