import adv_test
import adv

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'RR+15%buff_time & no s2'
    conf = {}
    if 0:
        conf['mod_wp'] = ('buff','time',0.15)
        conf['mod_wp2'] = [('crit','chance',0.08,'hp70'),
                        ('crit','damage',0.13) ]
    else:
        conf['mod_wp'] = ('buff','time',0.15)
        conf['mod_wp2'] = [('crit','chance',0.06,'hp70'),
                        ('s','damage',0.25) ]

    conf['mod_a1'] = ('crit', 'chance', 0.08, 'hp100')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

