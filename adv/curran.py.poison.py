import adv.curran
from slot.a import *
from slot.d import *

def module():
    return Curran

class Curran(adv.curran.Curran):
    comment = ''

    conf = adv.curran.Curran.conf.copy()
    conf['sim_afflict.time'] = 1
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = KFM()+The_Fires_of_Hate()
    conf['slots.d'] = Shinobi()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(module(), *sys.argv)