import core.condition as condition

def get(star,ele,wep):
    conf = {
            "mod_d"   : ('att'  , 'passive' , 0.60) ,
            "mod_wp"  :[('s'    , 'passive' , 0.25) ,
                        ('crit' , 'chance'  , 0.06  , 'hp70') ] ,
            "mod_wp2" :[('crit' , 'damage'  , 0.13) ,
                        ('crit' , 'chance'  , 0.08  , 'hp70') ] ,
            'str_wp'  : 64,
            'str_wp2' : 64,
            'str_d'   : 127*1.5,
            }


    if ele == 'shadow':
        conf['str_d'] = 121*1.5
    elif ele == 'light':
        conf['str_d'] = 119*1.5
    elif ele == 'water':
        conf['str_d'] = 125*1.5
        conf['mod_d'] = [('att' , 'passive', 0.45),
                         ('crit', 'chance' , 0.20)]

    if wep == 'sword':
        conf['mod_wp2'] = [('fs', 'passive' , 0.3) ,
                           ('s' , 'passive'  , 0.1)]
        conf['str_wp2'] = 52

    if wep == 'axe':
        conf['mod_wp2'] = [('crit' , 'chance' , 0.12),
                           ('s' , 'passive'  , 0.15)]
        conf['mod_wp'] = [('crit','chance',0.03,'hp70'),
                            ('s','passive',0.20)]

    if star == '3':
        conf['mod_wp2'] = []
        conf['str_wp2'] = 42

    conf['str_wp'] += conf['str_wp2']

    return conf
