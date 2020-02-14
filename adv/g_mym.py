import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return G_Mym

class G_Mym(Adv):
    a3 = ('dt', 0.20)

    conf = {}
    conf['slot.a'] = Resounding_Rendition()+An_Ancient_Oath()
    conf['slot.d'] = Sakuya()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2, fsc
        `fs, x=5
    """
    conf['dragonform1'] = {
        'act': 'c3 s',

        'dx1.dmg': 2.16,
        'dx1.startup': 20 / 60.0, # c1 frames
        'dx1.hit': 1,

        'dx2.dmg': 2.38,
        'dx2.startup': 48 / 60.0, # c2 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.03,
        'dx3.startup': 42 / 60.0, # c3 frames
        'dx3.recovery': 86 / 60.0, # recovery
        'dx3.hit': 1,

        'ds.dmg': 7.56,
        'ds.recovery': 142 / 60, # skill frames
        'ds.hit': 2,
    }
    conf['dragonform2'] = {
        'dx1.dmg': 2.32,
        'dx1.startup': 16 / 60.0, # c1 frames

        'dx2.dmg': 2.56,
        'dx2.startup': 44 / 60.0, # c2 frames

        'dx3.dmg': 3.25,
        'dx3.startup': 36 / 60.0, # c3 frames
        'dx3.recovery': 84 / 60.0, # recovery

        'ds.dmg': 11.62,
        'ds.recovery': 125 / 60, # skill frames
    }
    conf['dragonform'] = conf['dragonform1']
    def ds_proc(this):
        return this.dmg_make('d_ds',this.dragonform.conf.ds.dmg,'s')

    def prerun(this):
        this.a1_buff = Selfbuff('flamewyrm', 0.15, -1, 'att', 'passive')
        Event('dragon').listener(this.a1_on)

    def a1_on(this, e):
        if not this.a1_buff.get():
            this.a1_buff.on()
            this.dragonform.name = 'Super G_Mym'
            this.dragonform.conf += this.conf.dragonform2

    def s1_proc(this, e):
        this.dragonform.charge_gauge(5)

    def s2_proc(this, e):
        if this.a1_buff.get():
            this.dmg_make('o_s2_boost', 4.16)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)