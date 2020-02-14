import adv.adv_test
import adv.ieyasu
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(adv.ieyasu.Ieyasu):
    comment = ''
    conf = adv.ieyasu.Ieyasu.conf.copy()
    conf['sim_afflict.time'] = adv.adv_test.sim_duration
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = HoH()+The_Fires_of_Hate()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
