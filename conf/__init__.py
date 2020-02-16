import json
import conf.slot_common
from slot import Slots
from core import Conf

import conf.forte

fname = ''
find = '/'
if __file__.find('/') == -1:
    find = '\\'
    if __file__.find('\\') == -1:
        find = None
        fname = 'conf.json'
if find:
    l = __file__.rfind(find)
    fname = __file__[:l] + find + 'conf.json'

json_confs = None
with open(fname, 'r') as f:
    json_confs = json.load(f, parse_float=float, parse_int=int)

def get(name):
    conf = Conf()

    json_conf = Conf(json_confs.get(name))

    conf += json_conf
    
    import wep
    wt = conf.c.wt
    weapon = getattr(wep, wt)
    wepconf = Conf(weapon.conf)
    if bool(conf.c.lv2_autos):
        wepconf += Conf(weapon.lv2)

    conf += Conf(wepconf)

    return conf