import adv_test
from xander import *

def module():
    return Xander_best

class Xander_best(Xander):
    comment = 'together we stand & 10 stacks striker\'s strength'
    adv_name = 'Xander'
    conf = {
        "mod_a1"   : ('att'   , 'buff' , 0.30) ,
        "mod_a3"   : ('fs'   , 'passive' , 0.50) ,
        "mod_wp"   : [
            ('s'   , 'passive' , 0.15) ,
            ('att' , 'buff'    , 0.20) ,
            #('fs' , 'passive'   , 0.40) ,
            #('crit' ,'damage'  , 0.13) ,
            ('s' , 'passive'   , 0.20) ,
            ('crit' ,'chance'  , 0.06, 'hp70') ,
            ],
        "mod_wp2"   : [],
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
