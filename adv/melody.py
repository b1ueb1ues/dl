import adv_test
import adv

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'RR+15%buff_time & no s2'
    conf = {}
    conf['mod_wp2'] = ('buff','time',0.15)
    def pre(this):
        if this.condition('hp100'):
            this.conf['mod_a'] = ('crit' , 'passive', 0.08)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

