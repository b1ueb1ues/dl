import adv.adv_test
from core.advbase import Selfbuff
from core.timeline import now
from slot.d import Dreadking_Rathalos
from slot.a import Amulet, The_Lurker_in_the_Woods
import adv.chelsea

def module():
    return Chelsea

class Dear_Diary(Amulet):
    att = 65
    a = [('cc',0.14)]

class Chelsea(adv.chelsea.Chelsea):
    comment = 'roll fs; only use s1 3 times to proc RO at'
    conf = adv.chelsea.Chelsea.conf.copy()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = The_Lurker_in_the_Woods()+Dear_Diary()
    conf['acl'] = """
        `s3,not self.s3_buff
        `s2,fsc
        `s1,fsc and self.hp < 30 and self.ro_charges > 0
        `dodge, fsc
        `fs
    """

    def prerun(self):
        super().prerun()
        self.ro_charges = 3

    def dmg_before(self, name):
        hpold = self.hp
        super().dmg_before(name)
        if self.ro_charges > 0 and hpold > 30 and self.hp < 30:
            Selfbuff('resilient_offense',0.10, -1).on()
            self.comment += ' {}s'.format(round(now()))
            self.ro_charges -= 1

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)