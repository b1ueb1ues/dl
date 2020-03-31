import sys
import adv.erik
from slot.a import *
from slot.d import *

def module():
    return Erik

class Erik(adv.erik.Erik):
    comment = ''
    conf = adv.erik.Erik.conf.copy()
    conf['sim_afflict.time'] = 1
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = Kung_Fu_Masters()+The_Fires_of_Hate()
    conf['slots.d'] = Shinobi()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Erik, *sys.argv)
