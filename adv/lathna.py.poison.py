import adv.adv_test
import adv.lathna
from slot.a import *

def module():
    return Lathna

class Lathna(adv.lathna.Lathna):
    comment = ''
    conf = adv.lathna.Lathna.conf.copy()
    conf['sim_afflict.time'] = 180
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = Resounding_Rendition()+The_Plaguebringer()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)