import adv_test
import adv
from adv import *

def module():
    return Sinoa

class Sinoa(adv.Adv):
    conf = {
        "mod_a":('att','passive',0.13),
        'condition':'hp100',
            }

    def s1_proc(this, e):
        r = random.random()
        if r<0.25  :
            adv.Buff('s1_att',0.25,15*1.2,'att').on()
        elif r<0.5 :
            adv.Buff('s1_crit',0.25,10*1.2,'crit').on()
        else:
            log('failed','s1')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = '''
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        '''
    adv_test.test(module(), conf, verbose=0, mass=1)


