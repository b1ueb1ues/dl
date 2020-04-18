import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Orsem

class Orsem(Adv):
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')
    conf = {}
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, fsc
        `s3, fsc
        `fs, x=4
    """
    coab = ['Blade', 'Xander', 'Wand']

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

