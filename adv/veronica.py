import adv_test
import adv

def module():
    return Veronica

class Veronica(adv.Adv):
    a3 = ('prep','100%')
    def pre(this):
        if this.condition('hp70~hp71'):
            this.s1boost = 1.25*0.3
        else:
            this.s1boost = 1.25*0.3

    def init(this):
        adv.Teambuff('last',2.28,1).on()


    def s1_proc(this, e):
        if this.s1boost:
            this.dmg_make('o_s1_crisis', this.s1boost*10.84)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        `fs, seq=5 and s1.charged >= 2500
        """

    adv_test.test(module(), conf, verbose=0)

