import adv.xander
from core.advbase import *
from slot.a import *

def module():
    return Xander

class Here_Come_the_Sealers(Amulet):
    att = 65
    a = [('slayers',0.06),
         ('fs',0.50)]

class A_New_Look(Amulet):
    att = 65
    a = [('slayers_crit_chance',0.05),
         ('cd',0.17,'hp70')]

class Xander(adv.xander.Xander):
    comment = '10 stacks striker\'s strength'
    a1 = ('slayers',0.06)
    
    conf = adv.xander.Xander.conf.copy()
    conf['slots.a'] = Here_Come_the_Sealers() + A_New_Look()
    conf['slots.frostbite.a'] = conf['slots.a']
    coab = ['Blade', 'Yurius', 'Dagger']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Xander, *sys.argv)