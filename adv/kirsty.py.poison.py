import adv.adv_test
import adv.kirsty
from slot.a import *

def module():
    return Kirsty

class Kirsty(adv.kirsty.Kirsty):
    comment = ''

    conf = adv.kirsty.Kirsty.conf.copy()
    conf['sim_afflict.time'] = adv.adv_test.sim_duration
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = RR()+The_Fires_of_Hate()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)