import skillframe
import csv2conf
import copy
import slot_common
import forte
import slot
from core import Conf

conf = Conf()
conf.s1 = Conf()
conf.s2 = Conf()

def get_skillframe(name):
    global conf
    for i in skillframe.skills:
        sf = skillframe.skills[i]
        if name.lower() == i.lower():
            if sf[0] == '1':
                conf.s1.startup = 0.25
                conf.s1.recovery = 0.90
            else:
                conf.s1.recovery = float(sf[0])

            if sf[1] == '1':
                conf.s2.startup = 0.25
                conf.s2.recovery = 0.90
            else:
                conf.s2.recovery = float(sf[1])

def get(name):
    global conf

    get_skillframe(name)

    csvconf = csv2conf.get(name)

    conf += csvconf

    slots = slot.Slots()

    conf.slot_common = [slot_common.set]

    import wep
    wt = conf.c.wt
    weapon = getattr(wep, wt)
    wepconf = weapon.conf

    conf += wepconf

    return conf
    

