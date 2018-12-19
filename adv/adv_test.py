if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.log import *


mname = ""
def test(classname, conf, verbose):
    global mname
    classname(conf=conf).run(300)

    mname = classname.__name__
    if verbose:
        logcat()
    sum_dmg()
    return


def sum_dmg():
    l = logget()
    dmg_sum = {'x': 0, 's': 0  }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    xdmg_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0 }
    for i in l:
        if i[1] == 'dmg':
            #dmg_sum[i[2][0]] += i[3]
            if i[2][0] == 'x':
                dmg_sum['x'] += i[3]
            elif i[2][:2] == 's1':
                dmg_sum['s'] += i[3]
                sdmg_sum['s1']['dmg'] += i[3]
            elif i[2][:2] == 's2':
                dmg_sum['s'] += i[3]
                sdmg_sum['s2']['dmg'] += i[3]
            elif i[2][:2] == 's3':
                dmg_sum['s'] += i[3]
                sdmg_sum['s3']['dmg'] += i[3]
        elif i[1] == 'cast':
            if i[2] == 's1':
                sdmg_sum['s1']['count'] += 1
            elif i[2] == 's2':
                sdmg_sum['s2']['count'] += 1
            elif i[2] == 's3':
                sdmg_sum['s3']['count'] += 1
        elif i[1] == 'x' :
            xdmg_sum[i[2]] += 1

    total = dmg_sum['x'] + dmg_sum['s']
    dmg_sum['total'] = total
    xdmg_sum['x1'] -= xdmg_sum['x5']
    xdmg_sum['x2'] -= xdmg_sum['x5']
    xdmg_sum['x3'] -= xdmg_sum['x5']
    xdmg_sum['x4'] -= xdmg_sum['x5']

    xdmg_sum['x1'] -= xdmg_sum['x4']
    xdmg_sum['x2'] -= xdmg_sum['x4']
    xdmg_sum['x3'] -= xdmg_sum['x4']

    xdmg_sum['x1'] -= xdmg_sum['x3']
    xdmg_sum['x2'] -= xdmg_sum['x3']

    xdmg_sum['x1'] -= xdmg_sum['x2']
    tmp = xdmg_sum
    xdmg_sum = {}
    for i in tmp:
        if tmp[i] != 0:
            xdmg_sum[i] = tmp[i]

    sdmg_sum['s1'] = "dmg: %.2f (x%d)"%(sdmg_sum['s1']['dmg'], sdmg_sum['s1']['count'])
    sdmg_sum['s2'] = "dmg: %.2f (x%d)"%(sdmg_sum['s2']['dmg'], sdmg_sum['s2']['count'])
    sdmg_sum['s3'] = "dmg: %.2f (x%d)"%(sdmg_sum['s3']['dmg'], sdmg_sum['s3']['count'])

    global mname
    print '\n======================='
    print mname,dmg_sum['total']
    print '-----------------------'
    print "dmgsum     |", dmg_sum
    print "skill_stat |", sdmg_sum
    print "x_stat     |",xdmg_sum
