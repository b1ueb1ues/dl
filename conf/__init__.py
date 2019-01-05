import base_str
import skillframe
import equip_common

conf = {}
conf.update(base_str.conf)

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
    return conf
    

