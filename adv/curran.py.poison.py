import adv.adv_test
import adv.curran
from slot.a import *
from slot.d import *

def module():
    return Curran

class Curran(adv.curran.Curran):
    comment = ''

    conf = adv.curran.Curran.conf.copy()
    conf['sim_afflict.time'] = adv.adv_test.sim_duration
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = KFM()+The_Fires_of_Hate()
    conf['slots.d'] = Shinobi()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
