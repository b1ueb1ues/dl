import json
from slot import Slots
from core import Conf

import conf.halidom

def load_json(name):
    fname = ''
    find = '/'
    if __file__.find('/') == -1:
        find = '\\'
        if __file__.find('\\') == -1:
            find = None
            fname = name
    if find:
        l = __file__.rfind(find)
        fname = __file__[:l] + find + name

    with open(fname, 'r') as f:
        return json.load(f, parse_float=float, parse_int=int)

advconfs = load_json('advconf.json')
coability = load_json('chains.json')
skillshare = load_json('skillshare.json')

def coability_dict(ele):
    if ele:
        return {**coability['all'], **coability[ele]}
    else:
        return coability['all'].copy()

def get(name):
    conf = Conf()

    json_conf = Conf(advconfs.get(name))

    conf += json_conf
    
    import wep
    wt = conf.c.wt
    weapon = getattr(wep, wt)
    wepconf = Conf(weapon.conf)
    if bool(conf.c.lv2_autos):
        wepconf += Conf(weapon.lv2)

    conf += Conf(wepconf)

    return conf