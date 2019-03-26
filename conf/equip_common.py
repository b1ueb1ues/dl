import core.condition as condition

def get(star,ele,wep):
    conf = {
            "mod_d"   : ('att'  , 'passive' , 0.60) ,
            "mod_wp"  :[('s'    , 'passive' , 0.25)],
            "mod_wp2" :[('crit' , 'damage' , 0.13)] ,
            'str_wp' : 64,
            'str_wp2' : 64,
            'str_d'  : 127*1.5,
            }
    if condition.on('hp70'):
        conf['mod_wp' ].append(('crit','chance',0.06))
        conf['mod_wp2'].append(('crit','chance',0.08))

    if ele == 'shadow':
        conf['str_d'] = 121*1.5
    elif ele == 'light':
        conf['str_d'] = 119*1.5
    elif ele == 'water':
        conf['str_d'] = 125*1.5
        conf['mod_d'] = [('att' , 'passive', 0.45),
                         ('crit', 'chance' , 0.20)]

    if wep == 'sword':
        conf["mod_wp" ] = [('s' , 'passive' , 0.25)]
        conf['mod_wp2'] = [('fs', 'passive' , 0.3) ,
                           ('s' , 'passive'  , 0.1)]
        conf['str_wp2'] = 52

    if wep == 'axe':
        conf['mod_wp2'] = [('crit' , 'chance' , 0.12),
                           ('s' , 'passive'  , 0.15)]
        if condition.on('hp70'):
            conf['mod_wp'] = [('crit','chance',0.06),
                                ('s','passive',0.20)]
        else:
            conf['mod_wp'] = [('s','passive',0.20)]

    if star == '3':
        conf['mod_wp2'] = []
        conf['str_wp2'] = 42

    conf['str_wp'] += conf['str_wp2']

    return conf
