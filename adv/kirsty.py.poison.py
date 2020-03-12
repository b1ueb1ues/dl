import adv.kirsty
import sys
from slot.a import *

def module():
    return Kirsty

class Kirsty(adv.kirsty.Kirsty):
    comment = ''

    conf = adv.kirsty.Kirsty.conf.copy()
    conf['sim_afflict.time'] = 1
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = RR()+The_Fires_of_Hate()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Kirsty, *sys.argv)