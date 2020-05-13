from core.advbase import Selfbuff, SingleActionBuff
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
    conf['slots.d'] = Dreadking_Rathalos()
    conf['slots.a'] = The_Lurker_in_the_Woods()+Dear_Diary()
    conf['acl'] = """
        `s3,not self.s3_buff
        `s2,fsc
        `s1,fsc and self.hp < 30 and self.ro_charges > 0
        `dodge, fsc
        `fs
    """
    coab = ['Blade', 'Grace', 'Hunter_Berserker']

    def init(self):
        self.slots.c.coabs['Hunter_Berserker'] = [None, 'sword']

    def prerun(self):
        super().prerun()
        self.ro_charges = 3 if isinstance(self.slots.a.a2, Dear_Diary) else 0

        self.zerk_chain = None
        if 'Hunter_Berserker' in self.coab_list:
            self.zerk_chain = SingleActionBuff('zerk_chain', 0.20, 1, 'fs', 'buff')

    def dmg_before(self, name):
        hpold = self.hp
        super().dmg_before(name)
        if self.ro_charges > 0 and hpold > 30 and self.hp < 30:
            Selfbuff('resilient_offense',0.10, -1).on()
            self.comment += ' {}s'.format(round(now()))
            self.ro_charges -= 1
        if self.hp < 100 and self.zerk_chain is not None:
            self.zerk_chain.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    import sys
    test_with_argv(Chelsea, *sys.argv)