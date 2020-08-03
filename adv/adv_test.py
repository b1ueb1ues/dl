# /usr/bin/env python
# encoding:utf-8
from core.log import *
import time
import sys
import io
import csv
from contextlib import redirect_stdout

#import random
from core.condition import Condition
import multiprocessing

page = ''

sim_duration = 180
sim_times = 1000

team_dps = 16000

ex_str = '_'
ex_set = {}
ex_team_init = 0

def skill_efficiency(mod):
    return (team_dps * 1.25) * mod * 2 / 5 / sim_duration
tension_efficiency = {
    'energy': 0.5,
    'inspiration': 0.6
}


def set_ex(ex_string):
    global ex_set
    global ex_str
    ex_set = {}
    ex_str = ''

    ex_mapping = {
        'k': 'blade',
        'r': 'wand',
        'd': 'dagger',
        'b': 'bow',
        'm': 'axe2',
        's': 'sword',
        'g': 'geuden',
        't': 'tobias'
    }

    for e in ex_string:
        if e in ex_mapping:
            ex_str += e
            ex_name = ex_mapping[e]
            ex_set[ex_name] = ('ex', ex_name)

    if len(ex_str) == 0:
        ex_str = '_'


# if not sys.argv[0].endswith('flask') and len(sys.argv) >= 4:
#     set_ex(sys.argv[3])
#     ex_str = sys.argv[3]

mname = ""
base_str = 0
displayed_str = 0

g_condition = ""
g_condicomment = ''
comment = ""
dps = 0
bps = 0
real_duration = 0
dmax = 0
dmin = 0

def test(classname, conf, verbose=None, mass=None, duration=None, cond=None, ex=None, lines=None, special=False):
    global team_dps
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

    if duration:
        sim_duration = duration
    else:
        try:
            sim_duration = int(sys.argv[2])
        except:
            sim_duration = 180

    if verbose is not None:
        loglevel = verbose
    else:
        try:
            loglevel = int(sys.argv[1])
        except:
            loglevel = 0

    if ex is not None:
        ex_str = ex
        set_ex(ex_str)
    else:
        try:
            ex_str = sys.argv[3]
            set_ex(ex_str)
        except:
            pass 

    if mass is None:
        try:
            mass = int(sys.argv[4])
        except:
            pass

    a = time.time()
    if classname.name :
        mname = classname.name
    else:
        mname = classname.__name__

    if lines is None:
        lines = {}
        lines['_'] = []
        lines['k'] = []
        lines['r'] = []
        lines['kr'] = []

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
    adv = classname(conf=conf,cond=cond)
    adv.slots.c.ex.update(ex_set)
    real_duration = adv.run(sim_duration)

    if mass and loglevel <=0:
        if mass != 1:
            sim_times = mass
        r, real_duration = do_mass_sim(classname, conf, cond, ex_set, sim_duration)
    else:
        r = sum_dmg(real_duration)
    comment = adv.comment
    
    amulets = '['+adv.slots.a.__class__.__name__ + '+' + adv.slots.a.a2.__class__.__name__+']'
    amulets += '['+adv.slots.d.__class__.__name__+']'
    amulets += '['+adv.slots.w.__class__.__name__.split('_')[0]+']'
    #comment = amulets + comment

    if adv.condition.exist():
        r['condition'] = dict(adv.condition)
        condition = adv.condition.cond_str()
        g_condition = condition
    else:
        r['condition'] = None
        condition = ''

    displayed_str = adv.displayed_att
    base_str = adv.base_att
    

    if loglevel > 0 and loglevel & 1:
        logcat()
        sum_ac()

    if loglevel > 0 and loglevel & 2:
        print(adv._acl_str)

    if loglevel > 0 and loglevel & 4:
        if adv.conf['xtype'] == 'melee':
            logcat(['dmg','cancel','fs','cast','buff'])
        if adv.conf['xtype'] == 'ranged':
            logcat(['x','dmg','cancel','fs','cast','buff'])

    dps = r['dmg_sum']['total']/real_duration
    bps = r['buff_sum'] #* team_dps
    r['tension_sum'] = {k: round(v) for k, v in r['tension_sum'].items()}
    team_tension = r['tension_sum']

    r['logs'] = {}
    f = io.StringIO()
    with redirect_stdout(f):
        logcat([str(type(adv.slots.d).__name__), str(type(adv).__name__)])
    r['logs']['dragon'] = f.getvalue()
    f = io.StringIO()
    with redirect_stdout(f):
        sum_ac()
    r['logs']['action'] = f.getvalue()
    f = io.StringIO()
    dmg_sum, sdmg_sum, x_sum, o_sum, d_sum = summary(r)
    r['logs']['skill_stat'] = str(sdmg_sum)
    f = io.StringIO()
    with redirect_stdout(f):
        logcat()
    r['logs']['timeline'] = f.getvalue()

    recount = "%d"%(dps)
    if bps:
        recount += '(%.2f)'%bps
    for tension, count in team_tension.items():
        recount += '({}:{})'.format(tension, count)

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

        print("dmgsum     | "+ str(dmg_sum))
        print("skill_stat | "+ str(sdmg_sum))
        print("x_stat     | "+ str(x_sum))
        if r['o_sum']:
            print("others     | "+ str(o_sum))
        if r['dragon_sum']:
            print("dragon     | "+ str(d_sum))

    elif loglevel == -1:
        if condition != '':
            condition = '<%s>'%(condition)
        print("%s , %s (str: %d) %s ;%s ;%s"%( recount, mname, displayed_str,amulets, condition, comment ))
    elif loglevel == -2:
        print(report(condition, r, mname, adv, amulets))
    elif loglevel == -5:
        lines['_'].append(report(condition, r, mname, adv, amulets, special))
        lines['k'].append(report(condition, r, mname, adv, amulets, special, ex_mod='k'))
        lines['r'].append(report(condition, r, mname, adv, amulets, special, ex_mod='r'))
        lines['kr'].append(report(condition, r, mname, adv, amulets, special, ex_mod='kr'))
        if cond == False or condition == '':
            for ex in ('_', 'k', 'r', 'kr'):
                print('\n'.join(lines[ex]))

    if adv.condition.exist():
        r2 = test(classname, conf, verbose, mass, duration, False, lines=lines)
        g_condition = ''
        r['no_cond'] = r2
    elif g_condition != '':
        return r

    b = time.time()
    if loglevel > 0 and loglevel & 8:
        print('-----------------------\nrun in %f'%(b-a))
    elif loglevel < 0 and not loglevel-1 & 8:
        print('-----------------------\nrun in %f'%(b-a))
    return r

def summary(r):
        dmg_sum = {}
        sdmg_sum = {}
        o_sum = {}
        d_sum = {}
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

        for i in r['dragon_sum']:
            d_sum[i] = int(r['dragon_sum'][i])

        return dmg_sum, sdmg_sum, r['x_sum'], o_sum, d_sum

def report_dps_k(name, value):
    return value * 1.10

def report_dps_r(name, value):
    return value * 1.15 if (name[0] == 's' or name[0:2] == 'ds') else value

def report_dps_kr(name, value):
    return (value * 1.15 if (name[0] == 's' or name[0:2] == 'ds') else value) * 1.10

def report(condition, r, name, adv, amulets, special=False, ex_mod=None):
    global displayed_str
    global ex_str
    global comment
    global g_condition
    global sim_duration
    global real_duration

    if special:
        page = 'sp'
    else:
        page = str(sim_duration)

    report_csv = []
    report_csv.extend([
        '_c_'+name if condition == '' and g_condition != '' else name,
        adv.conf['c.stars']+'*',
        adv.conf['c.ele'],
        adv.conf['c.wt'],
        displayed_str,
        amulets,
        '!<{}>'.format(g_condition) if condition == '' and g_condition != '' else '<{}>'.format(condition),
        comment
    ])
    dps_mappings = {
        'attack': r['dmg_sum']['x']/real_duration,
        'force_strike': r['dmg_sum']['fs']/real_duration,
        'skill_1': r['sdmg_sum']['s1']['dmg']/real_duration,
        'skill_2': r['sdmg_sum']['s2']['dmg']/real_duration,
        'skill_3': r['sdmg_sum']['s3']['dmg']/real_duration,
        'team_buff': r['buff_sum']*team_dps
    }
    for tension, count in r['tension_sum'].items():
        dmg_val = count*skill_efficiency(tension_efficiency[tension])
        if dmg_val > 0:
            dps_mappings['team_{}'.format(tension)] = dmg_val
    for i in r['o_sum']:
        dmg_val = r['o_sum'][i]/real_duration
        if dmg_val > 0:
            dps_mappings[i] = dmg_val
    for i in r['dragon_sum']:
        dmg_val = r['dragon_sum'][i]/real_duration
        if dmg_val > 0:
            dps_mappings[i] = dmg_val
    dps_mod_f = None
    if ex_mod is not None:
        has_k = 'k' in ex_mod and adv.conf['c.wt'] != 'blade' and 'k' not in ex_str
        has_r = 'r' in ex_mod and adv.conf['c.wt'] != 'wand' and 'r' not in ex_str
        if has_k: 
            if has_r:
                dps_mod_f = report_dps_kr
            else:
                dps_mod_f = report_dps_k
        elif has_r:
            dps_mod_f = report_dps_r

    dps_sum = 0
    for name, value in dps_mappings.items():
        if dps_mod_f is not None and not name[0:4] == 'team':
            dps_mappings[name] = dps_mod_f(name, value)
        else:
            dps_mappings[name] = value
        dps_sum += dps_mappings[name]

    report_csv = [int(dps_sum)] + report_csv
    report_csv.extend(['{}:{}'.format(name, int(value)) for name, value in dps_mappings.items()])

    output_line = ','.join([str(s) for s in report_csv])
    if not condition == '' or not g_condition:
        real_ex = ex_str
        if ex_mod is not None: 
            if ex_str == '_':
                real_ex = ex_mod
            else:
                real_ex = ex_mod+ex_str
        output_line = ','.join(['-',page,real_ex])+'\n' + output_line
    return output_line

# def do_mass_sim_stub(sim_id, classname, conf, no_cond):
#     # print('SIM', 'cond', (not no_cond), sim_id)
#     global real_duration
#     global ex_set
#     print(sim_id, ex_set)
#     real_duration = 0
#     sum_duration = 0
#     if not no_cond:
#         adv = classname(conf=conf,cond=1)
#     else:
#         adv = classname(conf=conf,cond=0)
#     adv.slots.c.ex.update(ex_set)
#     from core.acl import do_act
#     adv._acl = do_act
#     real_duration = adv.run(sim_duration)
#     sum_duration += real_duration
#     #condi = adv.m_condition.p()
#     r = sum_dmg()
#     return r, sum_duration


# def do_mass_sim(classname, conf, no_cond=None):
#     global real_duration
#     global ex_set
#     results = []
#     adv = classname(conf=conf)
#     adv.slots.c.ex.update(ex_set)
#     adv.run(1)
#     # from core.acl import acl_func_str
#     # _acl_str = acl_func_str(adv.conf['acl'])
#     real_duration = 0
#     sum_duration = 0

#     with multiprocessing.Pool(processes=4) as pool:
#         for dat, sum_d in pool.starmap(do_mass_sim_stub, [(i, classname, conf, no_cond) for i in range(sim_times)]):
#             results.append(dat)
#             sum_duration += sum_d

#     real_duration = sum_duration / sim_times
#     r = sum_mass_dmg(results)
#     return r

def do_mass_sim_stub(sim_id, classname, conf, cond, ex_set, sim_duration):
    adv = classname(conf=conf,cond=cond)
    from core.acl import do_act
    adv._acl = do_act
    adv.slots.c.ex.update(ex_set)
    sum_d = adv.run(sim_duration)
    dat = sum_dmg(sum_d)
    return dat, sum_d

def do_mass_sim(classname, conf, cond, ex_set, sim_duration):
    results = []
    sum_duration = 0

    # Sequential version
    # for i in range(sim_times):
    #     dat, sum_d = do_mass_sim_stub(i, classname, conf, cond, ex_set, sim_duration)
    #     results.append(dat)
    #     sum_duration += sum_d

    with multiprocessing.Pool(processes=4) as pool:
        for dat, sum_d in pool.starmap(do_mass_sim_stub, [(i, classname, conf, cond, ex_set, sim_duration) for i in range(sim_times)]):
            results.append(dat)
            sum_duration += sum_d

    real_duration = sum_duration / sim_times
    r = sum_mass_dmg(results, real_duration)
    return r, real_duration


def sum_mass_dmg(rs, real_duration):
    global g_condicomment
    global dmax
    global dmin
    dmg_sum = {'x': 0, 's': 0, 'fs': 0, 'others':0, 'dragon': 0,'total': 0}
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    x_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0, "shift":0}
    o_sum = {}
    dragon_sum = {}
    team_buff = 0
    team_tension = {}

    dmax = 0
    dmin = 0

    for i in rs:
        for j in i['dmg_sum']:
            dmg_sum[j] += i['dmg_sum'][j] / sim_times
        for j in i['sdmg_sum'] :
            for k in i['sdmg_sum'][j]:
                sdmg_sum[j][k] += i['sdmg_sum'][j][k] / sim_times
        for j in i['x_sum'] :
            try:
                x_sum[j] += float(i['x_sum'][j]) / sim_times
            except:
                x_sum[j] = float(i['x_sum'][j]) / sim_times
        for j in i['o_sum'] :
            if j not in o_sum:
                o_sum[j] = 0
            o_sum[j] += i['o_sum'][j] / sim_times
        for j in i['dragon_sum'] :
            if j not in dragon_sum:
                dragon_sum[j] = 0
            dragon_sum[j] += i['dragon_sum'][j] / sim_times
        team_buff += i['buff_sum'] / sim_times
        
        case = 0
        case += i['dmg_sum']['total'] / real_duration
        case += i['buff_sum'] * team_dps

        for tension in ('energy', 'inspiration'):
            if tension in i['tension_sum']:
                if tension in team_tension:
                    team_tension[tension] += i['tension_sum'][tension]  / sim_times
                else:
                    team_tension[tension] = i['tension_sum'][tension]  / sim_times
                case += team_tension[tension] * skill_efficiency(tension_efficiency[tension])
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
    r['tension_sum'] = team_tension 
    r['dragon_sum'] = dragon_sum
    return r


def sum_ac():
    l = logget()
    prev = 0
    ret = []
    lastc = 0
    for i in l:
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
        if i[1] == 'dragon_start':
            lastc = 0
            ret.append('dragon')
    if lastc:
        ret.append(lastc)

    # print(ret)
    prev = 'c0'
    row = 0
    rowend = 20
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
                prin += '-'*(rowend - row)+i+' '
                row = 0
            else:
                prin += i+'\n'
            prev = 's'
        elif i[0] == 'c':
            if (prev == 's' or prev == 'd') and prin[-1] != '\n':
                row = 0
                prin += '\n'
            # elif prev == 'fs':
            #     row = 0
            #     prin += '\n'
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
            # if prev == 'fs':
            #     prin += '\nfs '
            #     row = 3
            # else:
            if prev == 's':
                prin += '\nfs '
                row = 3
            else:
                prin += 'fs '
                row += 3
            prev = 'fs'
        elif i == 'dragon':
            if len(prin) > 0 and prin[-1] != '\n':
                prin += '\n'
            prin += '------- dragon -------\n'
            prev = 'd'
            row = 0
    #if prev == 'c' :
    #    prin += i
    print(prin)

def sum_dmg(real_duration):
    l = logget()
    dmg_sum = {'x': 0, 's': 0, 'fs': 0, 'others':0, 'dragon': 0 }
    sdmg_sum = {'s1':{"dmg":0, "count": 0}, 
                's2':{"dmg":0, "count": 0}, 
                's3':{"dmg":0, "count": 0}, 
                }
    x_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0, "fs":0, "shift":0}
    dragon_sum = {'dx': 0}
    team_buff_powertime = 0
    team_buff_power = 0
    team_buff_start = 0
    team_tension = {}
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
            elif i[2][0] == 'd':
                dmg_sum['dragon'] += i[3]
                if i[2][0:2] == 'dx':
                    dragon_sum['dx'] += i[3]
                elif i[2] == 'dshift':
                    x_sum['shift'] += 1
                    dragon_sum['dx'] += i[3]
                else:
                    try:
                        dragon_sum[i[2]] += i[3]
                    except:
                        dragon_sum[i[2]] = i[3]
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
            try:
                x_sum[i[2]] += 1
            except:
                x_sum[i[2]] = 1
        elif i[1] == 'buff' and i[2] == 'team':
            if team_buff_power != 0:
                team_buff_powertime += team_buff_power*(i[0] - team_buff_start)
            team_buff_start = i[0]
            team_buff_power = i[3]
        elif i[1] in ('energy', 'inspiration') and i[2] == 'team':
            try:
                team_tension[i[1]] += i[3]
            except KeyError:
                team_tension[i[1]] = i[3]
    #print real_duration , team_buff_start, team_buff_power
    team_buff_powertime += (real_duration - team_buff_start)*team_buff_power


    total = dmg_sum['x'] + dmg_sum['s'] + dmg_sum['fs'] + dmg_sum['others'] + dmg_sum['dragon']
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
    r['tension_sum'] = team_tension
    r['dragon_sum'] = dragon_sum
    return r
