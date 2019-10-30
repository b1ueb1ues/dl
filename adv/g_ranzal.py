if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from module.fsalt import *
from slot.a import *

def module():
    return G_Ranzal


class G_Ranzal(Adv):
    comment = 'only s1'

    conf = {}
    conf['acl'] = """
        `s1, fsc
        `fs, seq=2 and this.gauges['x'] <= 500
        `fs, seq=3
    """
    conf['slots.a'] = JotS() + TSO()
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+BN()

    a3 = ('s',0.3)

    #c3 770
    #fs1 802
    #fs3 832
    #fsend 854-9
    #c1 854

    def prerun(this):
        this.ifs1ins2 = 0
        this.gauges = {
                'x':0,
                'fs':0,
                }
        this.fsacharge = -1
        this.fsa3conf = Conf()
        this.fsa3conf.fs = Conf(this.conf.fs)
        this.fsa3conf({
                'fs.dmg':0.83*2+0.92,
                'fs.sp' :330,
                "fs.startup":68/60.0,
                "x1fs.startup":77/60.0,
                "x2fs.startup":62/60.0,
                "x3fs.startup":62/60.0,

                "fs.recovery":13/60.0,
                "x1fs.recovery":13/60.0,
                "x2fs.recovery":13/60.0,
                "x3fs.recovery":13/60.0,
                })
        this.fsa1conf = Conf()
        this.fsa1conf.fs = Conf(this.conf.fs)
        this.fsa1conf({
                'fs.dmg':0.83,
                'fs.sp' :330,
                "fs.startup":33/60.0,
                "x1fs.startup":47/60.0,
                "x2fs.startup":32/60.0,
                "x3fs.startup":32/60.0,

                "fs.recovery":43/60.0,
                "x1fs.recovery":43/60.0,
                "x2fs.recovery":43/60.0,
                "x3fs.recovery":43/60.0,
                })
        this.fs_alt3 = Fs_alt(this, this.fsa3conf)
        this.fs_alt1 = Fs_alt(this, this.fsa1conf)
        this.fs_alt = this.fs_alt3
        #fs_alt_init(this, this.fsaconf)

        this.now = core.timeline.now

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.gauges['x'] += 77
        elif name == 'x2':
            this.gauges['x'] += 77
        elif name == 'x3':
            this.gauges['x'] += 100
        elif name == 'x4':
            this.gauges['x'] += 136
        elif name == 'x5':
            this.gauges['x'] += 200
        elif name == 'fs':
            this.gauges['fs'] += 150
        elif name == 'o_fs_alt':
            this.gauges['fs'] += 350
        log('debug','gauges',"%d, %d"%(this.gauges['x'],this.gauges['fs']), \
            "%d, %d"%(this.gauges['x'],this.gauges['fs']))

    def fs_proc(this, e):
        if this.fsacharge > 0:
            this.fsacharge -= 1
            if this.fsacharge == 0:
                this.fs_alt.off()
                this.fsacharge = -1

    def s1_proc(this, e):
        boost = 0
        if this.gauges['x'] >= 1000:
            boost += 1
            this.gauges['x'] = 0
        if this.gauges['fs'] >= 1000:
            boost += 1
            this.gauges['fs'] = 0
        if boost == 1:
            this.dmg_make('o_s1_boost',this.conf['s1.dmg']*0.2)
        if boost == 2:
            this.dmg_make('o_s1_boost',this.conf['s1.dmg']*0.8)
        this.ifs1ins2 = 1


    def s2_proc(this, e):
        this.fsacharge = 3
        this.fs_alt.on()
        this.ifs1ins2 = 0
        Event('defchain')()


    def s3_proc(this, e):
        Event('defchain')()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)
