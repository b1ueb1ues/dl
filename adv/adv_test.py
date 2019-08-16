# /usr/bin/env python
# encoding:utf-8
if __package__ is None or __package__ == '':
    import os
    os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.log import *
import time
import sys
import conf as globalconf
import random
from core import condition as m_condition
from core.acl import *

sim_duration = 180
if not sys.argv[0].endswith('flask') and len(sys.argv) >= 3:
    if sys.argv[2] == 'sp':
        sim_duration = 180
        page = 'sp'
    else:
        sim_duration = int(sys.argv[2])
        page = sys.argv[2]
sim_times = 1000

team_dps = 6000 
#team_dps = 5000

# 5000 raw skill damage, 0.5 bosst, 2 person, cost 5 stacks
energy_efficiency = 7500 * 0.5 * 2 / 5 / sim_duration 

katana = 0
ex_str = '_'
ex_set = {}
ex_team_init = 0

def set_ex(ex_str):
    global katana
    global ex_set
    global ex_team_init
    global team_dps
    global energy_efficiency
    katana = 0
    ex_set = {}
    ex_team_init = 0
    team_dps = 6000
    energy_efficiency = 7500 * 0.5 * 2 / 5 / sim_duration 
    for i in ex_str:
        if i == 'k':
            ex_set['blade'] = ('ex','blade')
            katana = 1
        elif i == 'r':
            ex_set['wand'] = ('ex','wand')
        elif i == 'd':
            ex_set['dagger'] = ('ex','dagger')
        elif i == 'b':
            ex_set['bow'] = ('ex','bow')

if not sys.argv[0].endswith('flask') and len(sys.argv) >= 4:
    set_ex(sys.argv[3])

mname = ""
base_str = 0
displayed_str = 0

g_condition = ""
g_condicomment = ''
comment = ""
dps = 0
bps = 0
real_duration = 0
line = ''
line_k = ''
dmax = 0
dmin = 0

def test(classname, conf, verbose=None, mass=0, duration=None, no_cond=None):
    global team_dps
    global energy_efficiency
    global mname
    global displayed_str
    global base_str
    global comment
    global g_condition
    global loglevel
    global sim_duration
    global real_duration
    global sim_times
    global ex_str
    global line
    global line_k

    if duration:
        sim_duration = duration

    if verbose is not None and loglevel == 0:
        loglevel = verbose
    #random.seed()
    a = time.time()
    if classname.name :
        mname = classname.name
    else:
        mname = classname.__name__

    if verbose == 255:
        loglevel = -2
    if loglevel == 255 and verbose:
        loglevel = -2
    if loglevel == -3 :
        loglevel = 255
        import module.ra
        module.ra.test(classname, conf, sim_duration)
        return
    if loglevel == -4 :
        loglevel = 255
        import module.racl
        module.racl.test(classname, conf, sim_duration)
        return


    global ex_set
    if not no_cond:
        adv = classname(conf=conf,cond=1)
    else:
        adv = classname(conf=conf,cond=0)
    adv.ex = ex_set
    comment = adv.comment

    real_duration = adv.run(sim_duration)

    global ex_team_init
    if not ex_team_init :
        ex_team_init = 1
        for i in adv.ex:
            if i == 'blade':
                team_dps *= 1.1
                energy_efficiency *= 1.1
            elif i == 'wand':
                team_dps *= 1.08
                energy_efficiency *= 1.15
            elif i == 'dagger':
                team_dps *= 1.07
                energy_efficiency *= 1.07
            elif i == 'bow':
                team_dps *= 1.05



    amulets = '['+adv.slots.a.__class__.__name__ + '+' + adv.slots.a.a2.__class__.__name__+']'
    amulets += '['+adv.slots.d.__class__.__name__+']'
    #comment = amulets + comment

    if not no_cond:
        condition = adv.m_condition.p()
    else:
        condition = ''
    if condition != '' :
        g_condition = condition

    displayed_str = adv.displayed_att
    base_str = adv.base_att
    

    if loglevel > 0 and loglevel & 1:
        logcat()
        sum_ac()

    if loglevel > 0 and loglevel & 2:
        print(adv._acl_str)

    if loglevel > 0 and loglevel & 4:
        if adv.conf['x_type'] == 'melee':
            logcat(['dmg','cancel','fs','cast','buff'])
        if adv.conf['x_type'] == 'ranged':
            logcat(['x','dmg','cancel','fs','cast','buff'])

    if mass and loglevel <=0 :
        if mass != 1:
            sim_times = mass
        r = do_mass_sim(classname,conf,no_cond)
    else:
        r = sum_dmg()

    dps = r['dmg_sum']['total']/real_duration
    bps = r['buff_sum'] #* team_dps
    team_energy = r['energy_sum'] #* energy_efficiency


    recount = "%d"%(dps)
    if bps:
        recount += '(%.2f)'%bps
    if team_energy:
        recount += '(team_energy:%d)'%team_energy

    if loglevel >= 0 or loglevel == None:
        if g_condition != '' and condition == '':
            print('-----------------------')
            print(recount+' !<%s>'%(g_condition))
            print('-----------------------')
        else:
            print('\n=======================')
            #print mname,"%d"%float_dps
            print("%s , %s (str: %d|%d) %s ;%s ;%s"%( recount, mname, 
                    base_str, displayed_str, amulets, '<%s>'%condition, comment ))
            print('-----------------------')

        dmg_sum = {}
        sdmg_sum = {}
        o_sum = {}
        for i in r['dmg_sum']:
            dmg_sum[i] = int(r['dmg_sum'][i])
        for i in r['sdmg_sum']:
            v = r['sdmg_sum'][i]
            if v['count'] :
                sdmg_sum[i] = '%d *%d = %d'%(int(v['dmg']/v['count']), v['count'], int(v['dmg']))
            else:
                sdmg_sum[i] = '%d'%(int(v['dmg']))

        for i in r['o_sum']:
            o_sum[i] = int(r['o_sum'][i])

        print("dmgsum     | "+ str(dmg_sum))
        print("skill_stat | "+ str(sdmg_sum))
        print("x_stat     | "+ str(r['x_sum']))
        if r['o_sum']:
            print("others     | "+ str(o_sum))

    elif loglevel == -1:
        if condition != '':
            condition = '<%s>'%(condition)
        print("%s , %s (str: %d) %s ;%s ;%s"%( recount, mname, displayed_str,amulets, condition, comment ))
    elif loglevel == -2:
        #comment += " (str: %d)"%(displayed_str)
        bdps = team_dps*bps
        name = mname
        exdps = team_dps + int(r['dmg_sum']['total']/real_duration)
        line = report__2(condition, exdps, r, name, adv, amulets)
        print(line)
    elif loglevel == -5:
        #comment += " (str: %d)"%(displayed_str)
        bdps = team_dps*bps
        name = mname
        exdps = team_dps + int(r['dmg_sum']['total']/real_duration)
        line += '\n'
        line += report__2(condition, exdps, r, name, adv, amulets)
        #print '-------'+line
        #print('-,%s,%s\n'%(sim_duration,ex_str)+line)
        if katana:
            print('cannot blade when -5')
            errrrrrrrrrrrrrrr()
        else:
            line_k += '\n'
            line_k += report__2_k(condition, exdps, r, name, adv, amulets)
            if no_cond or condition == '':
                output = '-,%s,%s'%(page, ex_str)
                if ex_str == '_' :
                    output_k = '-,%s,k'%(page)
                else:
                    output_k = '-,%s,k%s'%(page, ex_str)
                output += line
                output_k += line_k
                print(output)
                print(output_k)


    if condition != '':
        test(classname, conf, verbose, mass, duration, 1)
        g_condition = ''
    elif g_condition != '':
        return

    b = time.time()
    if loglevel > 0 and loglevel & 8:
        print('-----------------------\nrun in %f'%(b-a))
    elif loglevel < 0 and not loglevel-1 & 8:
        print('-----------------------\nrun in %f'%(b-a))
    return

def report__2(condition, exdps, r, name, adv, amulets):
    global mname
    global displayed_str
    global base_str
    global comment
    global g_condition
    global loglevel
    global sim_duration
    global real_duration
    global sim_times

    condi = ' '
    if condition != '':
        condition = '<%s>'%condition
        condi = condition
    else :
        if g_condition:
            name = '_c_'+mname
            condi = '!<%s>'%g_condition

    line = "%s,%s,%s,%s,%s,%s,%s,%s"%(
            name,adv.conf['c.stars']+'*', adv.conf['c.ele'], adv.conf['c.wt'], 
            displayed_str, amulets+g_condicomment ,condi,comment,
            )
    line = line.replace(',3*,',',3星,').replace(',4*,',',4星,').replace(',5*,',',5星,')
    line = line.replace(',sword,',',剑,').replace(',blade,',',刀,').replace(',axe,',',斧,').replace(',dagger,',',匕,')
    line = line.replace(',lance,',',枪,').replace(',wand,',',法,').replace(',bow,',',弓,')
    line = line.replace(',staff,',',奶,')
    line = line.replace(',shadow,',',暗,').replace(',light,',',光,')
    line = line.replace(',wind,',',风,').replace(',water,',',水,').replace(',flame,',',火,')
    line = '%d,'%(int(r['dmg_sum']['total']/real_duration+r['buff_sum']*team_dps+r['energy_sum']*energy_efficiency)) + line
    line += ',attack:%d'%(int(r['dmg_sum']['x']/real_duration))
    line += ',force_strike:%d'%(int(r['dmg_sum']['fs']/real_duration))
    line += ',skill_1:%d'%(int(r['sdmg_sum']['s1']['dmg']/real_duration))
    line += ',skill_2:%d'%(int(r['sdmg_sum']['s2']['dmg']/real_duration))
    line += ',skill_3:%d'%(int(r['sdmg_sum']['s3']['dmg']/real_duration))
    line += ',team_buff:%d'%(int(r['buff_sum']*team_dps))
    if r['energy_sum']:
        line += ',team_energy:%d'%(int(r['energy_sum']*energy_efficiency))
    if r['o_sum'] != {}:
        for i in r['o_sum']:
            line += ',%s:%d'%(i, int(r['o_sum'][i]/real_duration))
    return line

def report__2_k(condition, exdps, r, name, adv, amulets):
    global mname
    global displayed_str
    global base_str
    global comment
    global g_condition
    global g_condicomment
    global loglevel
    global sim_duration
    global real_duration
    global sim_times
    global dmin
    global dmax

    condi = ' '
    if condition != '':
        condition = '<%s>'%condition
        condi = condition
    else :
        if g_condition:
            name = '_c_'+mname
            condi = '!<%s>'%g_condition

    katana = 1.1
    if adv.conf['c.wt'] == 'blade':
        katana = 1.0

    if 0 < dmin < dmax:
        g_condicomment = ";dpsrange:(%d~%d)"%(dmin*1.1, dmax*1.1)

    line = "%s,%s,%s,%s,%s,%s,%s,%s"%(
            name,adv.conf['c.stars']+'*', adv.conf['c.ele'], adv.conf['c.wt'], 
            displayed_str, amulets+g_condicomment ,condi,comment,
            )
    line = line.replace(',3*,',',3星,').replace(',4*,',',4星,').replace(',5*,',',5星,')
    line = line.replace(',sword,',',剑,').replace(',blade,',',刀,').replace(',axe,',',斧,').replace(',dagger,',',匕,')
    line = line.replace(',lance,',',枪,').replace(',wand,',',法,').replace(',bow,',',弓,')
    line = line.replace(',staff,',',奶,')
    line = line.replace(',shadow,',',暗,').replace(',light,',',光,')
    line = line.replace(',wind,',',风,').replace(',water,',',水,').replace(',flame,',',火,')
    line = '%d,'%(int(katana*(r['dmg_sum']['total']/real_duration+r['buff_sum']*team_dps+r['energy_sum']*energy_efficiency))) + line
    line += ',attack:%d'%(int(katana*r['dmg_sum']['x']/real_duration))
    line += ',force_strike:%d'%(int(katana*r['dmg_sum']['fs']/real_duration))
    line += ',skill_1:%d'%(int(katana*r['sdmg_sum']['s1']['dmg']/real_duration))
    line += ',skill_2:%d'%(int(katana*r['sdmg_sum']['s2']['dmg']/real_duration))
    line += ',skill_3:%d'%(int(katana*r['sdmg_sum']['s3']['dmg']/real_duration))
    line += ',team_buff:%d'%(int(katana*r['buff_sum']*team_dps))
    if r['energy_sum']:
        line += ',team_energy:%d'%(int(katana*r['energy_sum']*energy_efficiency))
    if r['o_sum'] != {}:
        for i in r['o_sum']:
            line += ',%s:%d'%(i, int(katana*r['o_sum'][i]/real_duration))
    return line


def do_mass_sim(classname, conf, no_cond=None):
    global real_duration
    global ex_set
    results = []
    adv = classname(conf=conf)
    adv.ex = ex_set
    adv.run(1)
    _acl, _acl_str = acl_func_str(
                    adv.acl_prepare_default+adv.conf['acl'] 
                    )
    real_duration = 0
    sum_duration = 0
    for i in range(sim_times):
        if not no_cond:
            adv = classname(conf=conf,cond=1)
        else:
            adv = classname(conf=conf,cond=0)
        adv.ex = ex_set
        adv._acl = _acl
        real_duration = adv.run(sim_duration)
        sum_duration += real_duration
        #condi = adv.m_condition.p()
        r = sum_dmg()
        results.append(r)
    real_duration = sum_duration / sim_times
    r = sum_mass_dmg(results)
    return r

def sum_mass_dmg(rs):
    global g_condicomment
    global dmax
    global dmin
    dmg_sum = {'x': 0, 's': 0, 'fs': 0, 'others':0, 'total':0 }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    x_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0}
    o_sum = {}
    team_buff = 0
    team_energy = 0

    dmax = 0
    dmin = 0

    for i in rs:
        for j in i['dmg_sum'] :
            dmg_sum[j] += i['dmg_sum'][j] / sim_times
        for j in i['sdmg_sum'] :
            for k in i['sdmg_sum'][j]:
                sdmg_sum[j][k] += i['sdmg_sum'][j][k] / sim_times
        for j in i['x_sum'] :
            x_sum[j] += float(i['x_sum'][j]) / sim_times
        for j in i['o_sum'] :
            if j not in o_sum:
                o_sum[j] = 0
            o_sum[j] += i['o_sum'][j] / sim_times
        team_buff += i['buff_sum'] / sim_times
        team_energy += i['energy_sum']  / sim_times
        
        case = 0
        case += i['dmg_sum']['total'] / real_duration
        case += i['buff_sum'] * team_dps
        case += i['energy_sum'] * energy_efficiency
    #    print case
        if not dmin:
            dmin = case
        if case > dmax:
            dmax = case
        if case < dmin:
            dmin = case
    g_condicomment = ";dpsrange:(%d~%d)"%(dmin, dmax)

    for i in x_sum:
        x_sum[i] = int(x_sum[i]+0.01)
    r = {}
    r['dmg_sum'] = dmg_sum 
    r['sdmg_sum'] = sdmg_sum 
    r['x_sum'] = x_sum 
    r['o_sum'] = o_sum 
    r['buff_sum'] = team_buff  
    r['energy_sum'] = team_energy 
    return r



def statis(data, mname):
    total = 0
    dmin = data[0][0]
    dmax = data[0][0]
    bmin = data[0][1]
    bmax = data[0][1]
    size = len(data)
    buff_sum = 0
    energy_sum = 0
    for i in data:
        total += i[0]
        buff_sum += i[1]
        energy_sum += i[2]
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
    global energy
    global comment
    dps = float(total)/size
    bps = float(buff_sum)/size
    energy = float(energy_sum)/size
    if bps and bmin != bmax:
        comment = '(%.0f~%.0f)(%.2f~%.2f) %s'%(dmin, dmax, bmin, bmax, comment)
    else:
        comment = '(%.0f~%.0f) %s'%(dmin, dmax, comment)
    if energy:
        comment += '(team_energy:%.0f)'%energy

    #print("%d , %s (str: %d) %s ;(%.2f, %.2f) %s"%(total/size, mname, base_str, condition, dmin, dmax, comment))


def sum_ac():
    l = logget()
    prev = 0
    ret = []
    lastc = 0
    for i in l:
        if i[2] == 'succ':
            i[2] = 'fs'
        if i[1] == 'x':
            if i[2] == 'x1':
                if lastc != 0:
                    ret.append(lastc)
                    lastc = 'x1'
            if i[2] == 'x5':
                ret.append('c5')
                lastc = 0
            else:
                lastc = 'c'+i[2][1]
            prev = int(i[2][1])
        if i[1] == 'cast' or i[1] == 'fs' or i[1][:3] == 'fs_':
            lastc = 0
            if prev:
                if prev != 5:
                    ret.append("c%d"%prev)
                ret.append(i[2])
                prev = 0
            else:
                ret.append(i[2])
    if lastc:
        ret.append(lastc)

    print(ret)
    prev = 'c0'
    row = 0
    rowend = 11
    c5count = 0
    prin = ''
    for i in ret:
        if prev == 'c' and i[0] != 'c' and c5count!=0:
            if c5count == 1:
                prin += 'c5 '
                c5count = 0
                row += 3
            else:
                prin += 'c5*%d '%(c5count)
                c5count = 0
                row += 5

        if i[0] == 's':
            if prev != 's':
                prin += '-'*(rowend - row)+' '+i+' '
                row = 0
            else:
                prin += i+'\n'
            prev = 's'
        elif i[0] == 'c':
            if prev == 's':
                row = 0
                prin += '\n'
            elif prev == 'fs':
                row = 0
                prin += '\n'
            if i == 'c5':
                c5count+=1
            else:
                if c5count == 0:
                    prin += i+' '
                    row += 3
                elif c5count == 1:
                    prin += 'c5 %s '%(i)
                    c5count=0
                    row += 6
                else:
                    prin += 'c5*%d %s '%(c5count, i)
                    c5count=0
                    row += 8
            prev = 'c'
        elif i == 'fs':
            if prev == 'fs':
                prin += '\nfs '
                row = 3
            else:
                prin += 'fs '
                row +=3
            prev = 'fs'
    #if prev == 'c' :
    #    prin += i
    print(prin)

def sum_dmg():
    l = logget()
    dmg_sum = {'x': 0, 's': 0, 'fs': 0, 'others':0 }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    x_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0}
    team_buff_powertime = 0
    team_buff_power = 0
    team_buff_start = 0
    team_energy = 0
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
                x_sum['fs'] += 1
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
            x_sum[i[2]] += 1
        elif i[1] == 'buff' and i[2] == 'team':
            if team_buff_power != 0:
                team_buff_powertime += team_buff_power*(i[0] - team_buff_start)
            team_buff_start = i[0]
            team_buff_power = i[3]
        elif i[1] == 'energy' and i[2] == 'team':
            team_energy += i[3]
    #print real_duration , team_buff_start, team_buff_power
    team_buff_powertime += (real_duration - team_buff_start)*team_buff_power


    total = dmg_sum['x'] + dmg_sum['s'] + dmg_sum['fs'] + dmg_sum['others']
    dmg_sum['total'] = total
    x_sum['x1'] -= x_sum['x5']
    x_sum['x2'] -= x_sum['x5']
    x_sum['x3'] -= x_sum['x5']
    x_sum['x4'] -= x_sum['x5']

    x_sum['x1'] -= x_sum['x4']
    x_sum['x2'] -= x_sum['x4']
    x_sum['x3'] -= x_sum['x4']

    x_sum['x1'] -= x_sum['x3']
    x_sum['x2'] -= x_sum['x3']

    x_sum['x1'] -= x_sum['x2']
    tmp = x_sum
    x_sum = {}
    for i in tmp:
        if tmp[i] != 0:
            x_sum[i] = tmp[i]

    r = {}
    r['dmg_sum'] = dmg_sum
    r['sdmg_sum'] = sdmg_sum
    r['x_sum'] = x_sum
    r['o_sum'] = o_sum
    r['buff_sum'] = team_buff_powertime/real_duration
    r['energy_sum'] = team_energy
    return r

class Result(object):
    dmg_sum = {}
    sdmg_sum = {}
    x_sum = {}
    odmg_sum = {}
    bdmg_sum = 0
    energy_sum = 0





