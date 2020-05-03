import adv.xander
from core.advbase import *
from slot.a import *

def module():
    return Xander

class Wily_Warriors_Metal_and_Quick(Amulet):
    att = 55
    a = [('slayers',0.06),
         ('cd',0.22,'hp70')]

class A_New_Look(Amulet):
    att = 65
    a = [('slayers_crit_chance',0.05),
         ('cd',0.17,'hp70')]

class Xander(adv.xander.Xander):
    comment = '10 stacks striker\'s strength'
    a1 = ('slayers',0.06)
    
    conf = {}
    conf['slots.a'] = Wily_Warriors_Metal_and_Quick() + A_New_Look()
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, x=2 and cancel
        """
    coab = ['Blade','Wand','Dagger']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Xander, *sys.argv)