from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Patia

class Summer_Patia(Adv):
    comment = 'cannot build combo for Cat Sith; uses up 15 stacks by 46.94s'
    a3 = [('antiaffself_poison', 0.15, 10, 5), ('edge_poison', 60, 'hp50')]

    conf = {}
    conf['slots.poison.a'] = Kung_Fu_Masters()+The_Plaguebringer()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        # use dragon if using Cat Sith
        # `dragon.act('c3 s end'), fsc
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `s4, fsc
        `dodge, fsc
        `fs3
    """
    coab = ['Summer_Patia', 'Blade', 'Wand', 'Curran']
    share = ['Curran']

    def d_slots(self):
        if self.duration <= 120:
            self.conf['slots.d'] = Gala_Cat_Sith()

    def init(self):
        self.conf.fs.hit = -1
        conf_alt_fs = {
            'fs1': {
                'dmg': 207 / 100.0,
                'dmg2': 2.17,
                'sp': 600,
                'charge': 24 / 60.0,
                'startup': 24 / 60.0,
                'recovery': 46 / 60.0,
            },
            'fs2': {
                'dmg': 297 / 100.0,
                'dmg2': 3.12,
                'sp': 900,
                'charge': 48 / 60.0,
                'startup': 24 / 60.0,
                'recovery': 46 / 60.0,
            },
            'fs3': {
                'dmg': 384 / 100.0,
                'dmg2': 4.03,
                'sp': 1400,
                'charge': 72 / 60.0,
                'startup': 24 / 60.0,
                'recovery': 46 / 60.0,
            }
        }
        for n, c in conf_alt_fs.items():
            self.conf[n] = Conf(c)
            act = FS_MH(n, self.conf[n])
            self.__dict__['a_'+n] = act

        self.l_fs1 = Listener('fs1',self.l_fs1)
        self.l_fs2 = Listener('fs2',self.l_fs2)
        self.l_fs3 = Listener('fs3',self.l_fs3)
        self.fs = None
        self.fs_alt_uses = 0

    def do_fs(self, e, name):
        log('cast', name)
        e.name = name
        self.__dict__['a_'+name].getdoing().cancel_by.append(name)
        self.__dict__['a_'+name].getdoing().interrupt_by.append(name)
        self.fs_before(e)
        self.update_hits('fs')
        if self.fs_alt_uses:
            self.dmg_make(e.name, self.conf[name+'.dmg2'], 'fs')
            self.afflics.poison(e.name,110,0.436)
            self.fs_alt_uses = 0
        else:
            self.dmg_make(e.name, self.conf[name+'.dmg'], 'fs')
        self.fs_proc(e)
        self.think_pin('fs')
        self.charge(name,self.conf[name+'.sp'])

    def l_fs1(self, e):
        self.do_fs(e, 'fs1')

    def fs1(self):
        return self.a_fs1()

    def l_fs2(self, e):
        self.do_fs(e, 'fs2')

    def fs2(self):
        return self.a_fs2()

    def l_fs3(self, e):
        self.do_fs(e, 'fs3')

    def fs3(self):
        return self.a_fs3()

    def s1_before(self, e):
        self.dmg_make(e.name, 7.47)

    def s1_proc(self, e):
        self.dmg_make(e.name, 7.47)
        self.fs_alt_uses = 1

    def s2_proc(self, e):
        self.afflics.poison(e.name,120,0.582)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)