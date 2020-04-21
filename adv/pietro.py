from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Pietro

class Pietro(Adv):
#    comment = 'unsuitable resist'
    
    a1 = ('cd',0.13)

    conf = {}
    conf['slot.a'] = RR()+Breakfast_at_Valerios()
    conf['slots.frostbite.a'] = KFM()+His_Clever_Brother()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1
        `s3,seq=4
        `fs,seq=5
        """
    coab = ['Blade', 'Xander', 'Dagger']
    

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)