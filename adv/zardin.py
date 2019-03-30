import adv_test
import adv

def module():
    return Zardin

class Zardin(adv.Adv):
    comment = 'RR+tPoD'
    conf = {}
    conf['mod_a1'] = ('att', 'passive', 0.10, 'hp100')

    a = 2
    if a==1:
        conf["mod_wp"] = [('s','passive',0.25),
                         ('crit','chance',0.06,'hp70') ]
        conf["mod_wp2"] = [('fs','passive',0.40),
                           ('crit','damage',0.13) ]
    if a==2:
        conf["mod_wp"] = [('s','passive',0.25),
                         ('crit','chance',0.06,'hp70') ]
        conf["mod_wp2"] = [('crit','chance',0.09,'hit15'),
                           ('crit','damage',0.15) ]


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

