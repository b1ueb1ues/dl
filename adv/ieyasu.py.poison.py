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
    conf['slots.a'] = Heralds_of_Hinomoto()+The_Fires_of_Hate()
    def d_slots(self):
        if 'bow' in self.ex:
            self.conf.slot.a = Resounding_Rendition()+The_Fires_of_Hate()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
