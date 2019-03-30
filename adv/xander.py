import adv_test
import adv

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c2+fs & stella show + RR'
    conf = {
        "mod_a3": ('fs', 'passive', 0.50) ,
    } 

    a = 1
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
        `s1,fsc
        `s2,fsc
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)
    exit()

    module().conf['mod_wp'] = [('fs','passive',0.3),('s','passive',0.15)]
    adv_test.test(module(), conf, verbose=0)

    module().conf['mod_wp'] = [('s','passive',0.25)]
    adv_test.test(module(), conf, verbose=0)
