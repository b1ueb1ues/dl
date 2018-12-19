import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikoto21

class Mikoto21(adv.mikoto.Mikoto):
    pass

if __name__ == '__main__':
    conf = {}

    al = {
        #'sp': ["s1","s2"],
        'x5': ["s2"],
        'x4': ["s2"],
        'x3': ["s2"],
        'x2': ["s2"],
        'x1': ["s2"],
        's': ["s2", "s1","s3","s2"],
        } 

    conf['al'] = al

    adv_test.test(module(), conf, verbose=0)

