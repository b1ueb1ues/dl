# encoding:utf8
if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.log import *
import time
import sys
import conf as globalconf

sim_duration = 180
sim_times = 1000


ave_dps = 1500
mname = ""
base_str = 0
comment = ""
condition = ""
dps = 0
bps = 0
def test(classname, conf, verbose=0, mass=0):
    global mname
    global base_str
    global comment
    global condition
    a = time.time()
    mname = classname.__name__
    adv = classname(conf=conf)
    if mass :
        import random
        random.seed(0)
    adv.run(sim_duration)
    base_str = adv.conf['base_str']
    if 'condition' in adv.conf:
        condition = adv.conf['condition']
    comment = adv.comment


    if loglevel != None:
        verbose = loglevel

    if verbose > 0:
        logcat()
        sum_ac()
    elif verbose == 3:
        if adv.conf['x_type'] == 'melee':
            logcat(['dmg','cancel','fs','cast','buff'])
        if adv.conf['x_type'] == 'ranged':
            logcat(['x','dmg','cancel','fs','cast','buff'])

    if mass:
        if loglevel != -1:
            r = sum_dmg()
        do_mass_sim(classname, conf)
    else:
        r = sum_dmg()

    if loglevel >= 0 or loglevel == None:
        print '\n======================='
        #print mname,"%d"%float_dps
        print "%d(%.2f) , %s (str: %d) %s ;%s"%( dps, bps, mname, base_str, condition, comment )
        print '-----------------------'
        print "dmgsum     |", r['dmg_sum']
        print "skill_stat |", r['sdmg_sum']
        print "x_stat     |", r['xdmg_sum']
        if r['o_sum']:
            print "others     |", r['o_sum']
    elif loglevel == -1:
        print "%d(%.2f) , %s (str: %d) %s ;%s"%( dps, bps, mname, base_str, condition, comment )
    elif loglevel == -2:
        line = "%s,%s,%s,%s,%s,%d,%d"%( mname,adv.conf['stars'], adv.conf['element'], adv.conf['weapon'], condition+';'+comment,dps, dps+ave_dps*2.5*bps)
        line = line.replace(',3,',',3星,').replace(',4,',',4星,').replace(',5,',',5星,')
        line = line.replace('sword','剑').replace('blade','刀').replace('axe','斧').replace('dagger','匕')
        line = line.replace('lance','枪').replace('wand','法').replace('bow','弓')
        line = line.replace('shadow','暗').replace('light','光')
        line = line.replace('wind','风').replace('water','水').replace('flame','火')
        print line

    b = time.time()
    if loglevel >= 2:
        print '-----------------------\nrun in %f'%(b-a)
    return


def statis(data, mname):
    total = 0
    dmin = data[0][0]
    dmax = data[0][0]
    bmin = data[0][1]
    bmax = data[0][1]
    size = len(data)
    buff_sum = 0
    for i in data:
        total += i[0]
        buff_sum += i[1]
        if i[0] < dmin:
            dmin = i[0]
        if i[0] > dmax:
            dmax = i[0]
        if i[1] < bmin:
            bmin = i[1]
        if i[1] > bmax:
            bmax = i[1]
    
    global dps
    global bps
    global comment
    dps = total/size
    bps = buff_sum/size
    if bps:
        comment = '(%.0f~%.0f)(%.2f~%.2f) %s'%(dmin, dmax, bmin, bmax, comment)
    else:
        comment = '(%.0f~%.0f) %s'%(dmin, dmax, comment)
    #print "%d , %s (str: %d) %s ;(%.2f, %.2f) %s"%(total/size, mname, base_str, condition, dmin, dmax, comment)

def do_mass_sim(classname, conf):
    a = time.time()
    mname = classname.__name__

    results = []
    for i in range(sim_times):
        adv = classname(conf=conf)
        adv.run(sim_duration)
        r = sum_dmg(1)
        results.append(r)
    statis(results, mname)

    b = time.time()
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
    print ''

def sum_dmg(silence=0):
    l = logget()
    dmg_sum = {'x': 0, 's': 0, 'fs': 0, 'others':0 }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    xdmg_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0}
    team_buff_powertime = 0
    team_buff_power = 0
    team_buff_start = 0
    o_sum = {}
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
            elif i[2][0] == 'o':
                dmg_sum['others'] += i[3]
                if i[2][2:] in o_sum:
                    o_sum[i[2][2:]] += i[3]
                else:
                    o_sum[i[2][2:]] = i[3]

        elif i[1] == 'cast' or i[1] == 's':
            if i[2] == 's1':
                sdmg_sum['s1']['count'] += 1
            elif i[2] == 's2':
                sdmg_sum['s2']['count'] += 1
            elif i[2] == 's3':
                sdmg_sum['s3']['count'] += 1
        elif i[1] == 'x' :
            xdmg_sum[i[2]] += 1

        elif i[1] == 'buff' and i[2] == 'team':
            if team_buff_power != 0:
                team_buff_powertime += team_buff_power*(i[0] - team_buff_start)
            team_buff_start = i[0]
            team_buff_power = i[3]
    team_buff_powertime += (sim_duration - team_buff_start)*team_buff_power


    total = dmg_sum['x'] + dmg_sum['s'] + dmg_sum['fs'] + dmg_sum['others']
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

    global dps
    global bps
    dps = dmg_sum['total']/sim_duration
    bps = team_buff_powertime/sim_duration
    if silence:
        return dps, bps

    for i in dmg_sum:
        dmg_sum[i] = '%.0f'%dmg_sum[i]
    for i in sdmg_sum:
        sdmg_sum[i] = "%.0f (%d)"%(sdmg_sum[i]['dmg'], sdmg_sum[i]['count'])
    for i in o_sum:
        o_sum[i] = "%.0f"%(o_sum[i])
    
    r = {}
    r['dmg_sum'] = dmg_sum
    r['sdmg_sum'] = sdmg_sum
    r['xdmg_sum'] = xdmg_sum
    r['o_sum'] = o_sum
    r['buff_sum'] = team_buff_powertime/sim_duration

    #if loglevel >= 0 or loglevel == None:
    #    print '\n======================='
    #    #print mname,"%d"%float_dps
    #    print "%d , %s (str: %d) %s ;%s"%( float_dps, mname, base_str, condition, comment )
    #    print '-----------------------'
    #    print "dmgsum     |", dmg_sum
    #    print "skill_stat |", sdmg_sum
    #    print "x_stat     |", xdmg_sum
    #    print "others     |", o_sum
    #elif loglevel == -1:
    #    print "%d , %s (str: %d) %s ;%s"%( float_dps, mname, base_str, condition, comment )
    return r
