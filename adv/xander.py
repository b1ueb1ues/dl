import adv.adv_test
from core.advbase import *
from slot.a import *
import slot.a
from slot.d import *

def module():
    return Xander

class Xander(Adv):
    a3 = ('fs',0.50)
    comment = 'c2+fs'
    conf = {}
    conf['slots.a'] = TSO()+Primal_Crisis()
    conf['slots.d'] = Siren()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=2 and cancel
        """
    coab = ['Xainfried', 'Pipple', 'Dagger']
    def s1_proc(self, e):
        self.dmg_make('o_s1_boost',self.conf['s1.dmg']*0.05*len(self.all_buffs))

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

