import adv_test
import adv

def module():
    return Xander

class Xander(adv.Adv):
    conf = {
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        "mod_a"   : ('fs'   , 'passive' , 0.50) ,

        "mod_wp"   : [
            ('fs'   , 'passive' , 0.30) ,
            ('sp'   , 'passive' , 0.08) ,
            ]
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)
    exit()

    module().conf['mod_wp'] = [('fs','passive',0.3),('s','passive',0.15)]
    adv_test.test(module(), conf, verbose=0)

    module().conf['mod_wp'] = [('s','passive',0.25)]
    adv_test.test(module(), conf, verbose=0)
