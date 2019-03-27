import adv_test
import adv

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c2+fs'
    conf = {
        "mod_a3": ('fs', 'passive', 0.50) ,
    } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0, mass=0)
    exit()

    module().conf['mod_wp'] = [('fs','passive',0.3),('s','passive',0.15)]
    adv_test.test(module(), conf, verbose=0)

    module().conf['mod_wp'] = [('s','passive',0.25)]
    adv_test.test(module(), conf, verbose=0)
