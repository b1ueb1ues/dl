import skillframe
import equip_common
import csv2conf

conf = {}

def get_advconf(name):
    return


def get_skillframe(name):
    global conf
    for i in skillframe.skills:
        sf = skillframe.skills[i]
        if name.lower() == i.lower():
            if sf[0] == '1':
                conf.update({
                        "s1_startup":0.25,
                        "s1_recovery":0.9,
                        })
            else:
                conf.update({
                        "s1_recovery":float(sf[0]),
                        })
            if sf[1] == '1':
                conf.update({
                        "s2_startup":0.25,
                        "s2_recovery":0.9,
                        })
            else:
                conf.update({
                        "s2_recovery":float(sf[1]),
                        })

def get(name):
    get_advconf(name)
    get_skillframe(name)
    conf.update(equip_common.conf)
    csvconf = csv2conf.get(name)
    conf.update(csvconf)
    if conf['weapon']=='sword':
        import wep.sword as weapon
    elif conf['weapon']=='blade':
        import wep.blade as weapon
    elif conf['weapon']=='dagger':
        import wep.dagger as weapon
    elif conf['weapon']=='axe':
        import wep.axe as weapon
    elif conf['weapon']=='lance':
        import wep.lance as weapon
    elif conf['weapon']=='bow':
        import wep.bow as weapon
    elif conf['weapon']=='wand':
        import wep.wand as weapon

    wepconf = getattr(weapon,conf['element'])

    conf.update(wepconf.conf)
    base_str = conf['str_d']+conf['str_wp']+conf['str_w']

    if conf['element'] == 'flame':
        base_str += conf['str_adv'] * (1+0.15+0.23)
    elif conf['element'] == 'water':
        base_str += conf['str_adv'] * (1+0.22+0.23)
    elif conf['element'] == 'wind':
        base_str += conf['str_adv'] * (1+0.22+0.23)
    elif conf['element'] == 'light':
        base_str += conf['str_adv'] * (1+0.22+0.23)
    elif conf['element'] == 'shadow':
        base_str += conf['str_adv'] * (1+0.15+0.23)

    conf['base_str'] = int(base_str)
    return conf
    

