import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Pietro

class Pietro(Adv):
    a1 = ('cd',0.13)
#    comment = 'unsuitable resist'
    conf = {}
    conf['slot.a'] = RR()+Breakfast_at_Valerios()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s3,seq=4
        `fs,seq=5
        """
    coab = ['Blade', 'Xander', 'Dagger']

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

