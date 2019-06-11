import adv_test
from adv import *
from slot.a import *

def module():
    return G_Mym

class G_Mym(Adv):
    comment = 'get a1 boost half way; no dragon(see special page with dragon)'

    conf = {}
    conf['slot.a'] = RR()+Jewels_of_the_Sun()
    #conf['slot.a'] = RR()+Worthy_Rivals()
    #import slot
    #conf['slots.d'] = slot.d.flame.Sakuya()



    def init(this):
        this.dp = 0
        this.truemumu = 0
        timing = adv_test.sim_duration/2
        Timer(this.dragon).on(timing)
        #this.dragon(0)

    def s1_proc(this, e):
        this.dp += 5
        if this.dp > 100:
            this.dp = 100
        log('debug','dp',this.dp)

    def s2_proc(this, e):
        if this.truemumu :
            this.dmg_make('o_s2_boost', 4.16)

    def dragon(this, t):
        if not this.truemumu:
            pass
            this.truemumu = 1
            Buff('a1',0.15,-1).on()
        else:
            pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)


