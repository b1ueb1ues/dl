import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Jakob

class Jakob(Adv):
    a1 = ('prep','50%')

    conf = {}
    conf['slot.a'] = RR()+Breakfast_at_Valerios()
    conf['acl'] = """
        `dragon
        `s1
        `s3,fsc
        `fs,seq=5
        """
    coab = ['Blade', 'Xander', 'Dagger']
    conf['slot.d'] = Leviathan()
    conf['afflict_res.bog'] = 100

    def s1_proc(self, e):
        self.dmg_make('s1',2.27)
        self.afflics.bog.on('s1', 90)
        self.dmg_make('s1',4.54)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

