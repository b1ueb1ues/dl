import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Dragonyule_Nefaria

class Dragonyule_Nefaria(Adv):
    a1 = ('s',0.25)
    conf = {}
    conf['slot.a'] = Mega_Friends()+Primal_Crisis()
    conf['acl'] = """
        `dragon
        `s1, fsc
        `s3, fsc
        `fs, seq=4
        """
    coab = ['Blade', 'Xander', 'Thaniel']
    conf['slots.d'] = Leviathan()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

