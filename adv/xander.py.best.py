import adv_test
import adv

def module():
    return Xander

class Xander(adv.Adv):
    conf = {
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,

        "mod_a"   : ('fs'   , 'passive' , 0.50) ,

        "mod_a2"   : ('att'   , 'buff' , 0.30) ,

        "mod_wp"   : [
            ('s'   , 'passive' , 0.15) ,
            ('att' , 'buff'    , 0.20) ,
            ],
        } 

    def s1_proc(this,e):
        this.dmg_make('s1_boost',this.conf['s1_dmg']*0.5)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0)
    exit()

    module().conf['mod_wp'] = [('fs','passive',0.3),('s','passive',0.15)]
    adv_test.test(module(), conf, verbose=0)

    module().conf['mod_wp'] = [('s','passive',0.25)]
    adv_test.test(module(), conf, verbose=0)
