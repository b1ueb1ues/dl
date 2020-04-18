import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Luther

class Luther(Adv):
    a1 = ('cc',0.10,'hit15')
    conf = {}
    conf ['slot.a'] = Twinfold_Bonds()+ The_Prince_of_Dragonyule()
    conf ['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    coab = ['Blade', 'Xander', 'Wand']

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

