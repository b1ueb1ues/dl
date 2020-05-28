from core.advbase import *
from module.x_alt import Fs_alt
from slot.a import *
from slot.d import *

def module():
    return Gala_Ranzal

class Gala_Ranzal(Adv):
    comment = 'no s2'

    conf = {}
    conf['slots.a'] = The_Shining_Overlord()+United_by_One_Vision()
    conf['slots.d'] = AC011_Garland()
    conf['acl'] = '''
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1, fsc
        `fs, seq=2 and self.gauges['x'] <= 500
        `fs, seq=3
    '''
    coab = ['Blade','Dragonyule_Xainfried','Lin_You']
    
    a3 = ('s',0.3)

    #c3 770
    #fs1 802
    #fs3 832
    #fsend 854-9
    #c1 854

    def prerun(self):
        self.ifs1ins2 = 0
        self.gauges = {
                'x':0,
                'fs':0,
                }
        self.conf.fs.gauge = 150
        conf_fs_alt = {
            'fs.dmg':0.83*2+0.92,
            'fs.sp' :330,
            'fs.gauge': 350,
            'fs.charge': 2/60.0, # needs confirm
            'fs.startup':66/60.0,
            'x1fs.startup':75/60.0,
            'x2fs.startup':60/60.0,
            'x3fs.startup':60/60.0,

            'fs.recovery':13/60.0,
            'x1fs.recovery':13/60.0,
            'x2fs.recovery':13/60.0,
            'x3fs.recovery':13/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))

    def dmg_proc(self, name, amount):
        if name == 'x1':
            self.gauges['x'] += 77
        elif name == 'x2':
            self.gauges['x'] += 77
        elif name == 'x3':
            self.gauges['x'] += 100
        elif name == 'x4':
            self.gauges['x'] += 136
        elif name == 'x5':
            self.gauges['x'] += 200
        elif name == 'fs':
            self.gauges['fs'] += self.conf.fs.gauge
        log('gauges', name, self.gauges['x'], self.gauges['fs'])

    def s1_proc(self, e):
        try:
            boost = 0
            if self.gauges['x'] >= 1000:
                boost += 1
                self.gauges['x'] = 0
            if self.gauges['fs'] >= 1000:
                boost += 1
                self.gauges['fs'] = 0
            if boost == 1:
                self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.2)
            if boost == 2:
                self.dmg_make(f'o_{e.name}_boost',self.conf[f'{e.name}.dmg']*0.8)
            self.ifs1ins2 = 1
        except:
            pass


    def s2_proc(self, e):
        self.fs_alt.on(3)
        self.ifs1ins2 = 0
        Event('defchain')()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)