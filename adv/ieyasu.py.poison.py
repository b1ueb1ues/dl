import sys
import adv.ieyasu
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(adv.ieyasu.Ieyasu):
    comment = ''
    conf = adv.ieyasu.Ieyasu.conf.copy()
    conf['sim_afflict.time'] = 1
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = Heralds_of_Hinomoto()+The_Fires_of_Hate()
    def d_slots(self):
        if 'bow' in self.ex:
            self.slots.a = Resounding_Rendition()+The_Fires_of_Hate()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Ieyasu, *sys.argv)