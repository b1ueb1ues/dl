if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.log import *
import time


mname = ""
def test(classname, conf, verbose):
    global mname
    a = time.time()
    classname(conf=conf).run(300)
    b = time.time()

    mname = classname.__name__
    import sys
    if len(sys.argv) >= 2:
        verbose = sys.argv[1]
    verbose = int(verbose)

    if verbose != 0:
        logcat()
        sum_ac()
    sum_dmg()
    if loglevel >= 2:
        print '-----------------------\nrun in %f'%(b-a)
    return

def sum_ac():
    l = logget()
    prev = 0
    ret = []
    for i in l:
        if i[1] == 'x':
            if i[2] == 'x5':
                ret.append('c5')
            prev = int(i[2][1])
        if i[1] == 'cast' or i[1] == 'fs':
            if prev:
                if prev != 5:
                    ret.append("c%d"%prev)
                ret.append(i[2])
                prev = 0
            else:
                ret.append(i[2])
    #print ret
    prev = 'c0'
    row = 0
    c5count = 0
    for i in ret:
        if prev == 's':
            if i[0] == 's':
                print '%s'%i,
            elif i[0] == 'c' :
                print '\n',
                prev = 'c5'
        elif i[0] == 's':
            if i == 'succ': i = 'fs'
            if prev == 'c5':
                print 'c5*%d    - %s'%(c5count, i) ,
            elif prev == 'c0':
                print '        - %s'%(i) ,
            else:
                print '- %s'%(i) ,
            prev = 's'
            c5count = 0
            #if row >= 8:
            #    print '\t`%s'%i,
            #if row < 8:
            #    print '\t\t`%s'%i,
            row =0
        if i[0] == 'c':
            if i == 'c5':
                prev = i
                c5count+=1
            else:
                prev = i
                if c5count == 0:
                    print '     %s'%(i),
                else:
                    print 'c5*%d %s'%(c5count, i),
            #print i,
            row += 3

def sum_dmg():
    l = logget()
    dmg_sum = {'x': 0, 's': 0, 'fs': 0 }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    xdmg_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0}
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
            elif i[2][:2] == 'fs':
                dmg_sum['fs'] += i[3]
                xdmg_sum['fs'] += 1
        elif i[1] == 'cast':
            if i[2] == 's1':
                sdmg_sum['s1']['count'] += 1
            elif i[2] == 's2':
                sdmg_sum['s2']['count'] += 1
            elif i[2] == 's3':
                sdmg_sum['s3']['count'] += 1
        elif i[1] == 'x' :
            xdmg_sum[i[2]] += 1

    total = dmg_sum['x'] + dmg_sum['s'] + dmg_sum['fs']
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

    for i in dmg_sum:
        dmg_sum[i] = '%.3f'%dmg_sum[i]

    for i in sdmg_sum:
        sdmg_sum[i] = "%.2f (%d)"%(sdmg_sum[i]['dmg'], sdmg_sum[i]['count'])


    global mname
    print '\n======================='
    print mname,dmg_sum['total']
    print '-----------------------'
    print "dmgsum     |", dmg_sum
    print "skill_stat |", sdmg_sum
    print "x_stat     |",xdmg_sum
