import sys
import os
import re

BR = 64
BLADE = 1.10
WAND = 1.15
def skill_efficiency(real_d, team_dps, mod):
    return (team_dps * 1.25) * mod * 2 / 5 / real_d
tension_efficiency = {
    'energy': 0.5,
    'inspiration': 0.6
}
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

def blade_mod(name, value):
    if 'team' in name:
        return value
    else:
        return value * BLADE

def wand_mod(name, value):
    if name[0] == 's' or name == 'ds':
        return value * WAND
    else:
        return value

def blade_wand_mod(name, value):
    return blade_mod(name, wand_mod(name, value))

def parse_ex(ex):
    ex_set = {}
    for e in ex:
        try:
            ex_name = ex_mapping[e]
            ex_set[ex_name] = ('ex', ex_name)
        except:
            continue
    return ex_set

def build_exp_mod_list(ex, ex_set, wt):
    if ex == '_':
        ex = ''
        ex_mod_func = [('_', None)]
    else:
        ex_mod_func = [('', None)]
    if 'blade' not in ex_set and wt != 'blade':
        ex_mod_func.append(('k', blade_mod))
        has_k = True
    else:
        ex_mod_func.append(('k', None))
        has_k = False
    if 'wand' not in ex_set and wt != 'wand':
        ex_mod_func.append(('r', wand_mod))
        has_r = True
    else:
        ex_mod_func.append(('r', None))
        has_r = False
    if has_k and has_r:
        ex_mod_func.append(('kr', blade_wand_mod))
    elif has_k:
        ex_mod_func.append(('kr', blade_mod))
    elif has_r:
        ex_mod_func.append(('kr', wand_mod))
    else:
        ex_mod_func.append(('kr', None))
    return ex_mod_func, ex

def run_once(classname, conf, duration, cond):
    adv = classname(conf=conf,cond=cond)
    real_d = adv.run(duration)
    return adv, real_d

# Using starmap
import multiprocessing
def run_once_mass(classname, conf, duration, cond, idx):
    adv = classname(conf=conf,cond=cond)
    from core.acl import do_act
    adv._acl = do_act
    real_d = adv.run(duration)
    return adv.logs, real_d

def sum_logs(log, other):
    for k1 in log.damage:
        for k2 in log.damage[k1]:
            log.damage[k1][k2] += other.damage[k1][k2]
    log.team_buff += other.team_buff
    for k in log.team_tension:
        log.team_tension[k] += other.team_tension[k]
    return log

def avg_logs(log, mass):
    for k1 in log.damage:
        for k2 in log.damage[k1]:
            log.damage[k1][k2] /= mass
    log.team_buff /= mass
    for k in log.team_tension:
        log.team_tension[k] /= mass
    return log

def run_mass(mass, base_log, base_d, classname, conf, duration, cond):
    mass = 1000 if mass == 1 else mass
    with multiprocessing.Pool(processes=8) as pool:
        for log, real_d in pool.starmap(run_once_mass, [(classname, conf, duration, cond, idx) for idx in range(mass-1)]):
            base_log = sum_logs(base_log, log)
            base_d += real_d
    base_log = avg_logs(base_log, mass)
    base_d /= mass
    return base_log, base_d

def test(classname, conf={}, ex='_', duration=180, verbose=0, mass=None, output=None, team_dps=None, cond=True, special=False):
    team_dps = team_dps if team_dps is not None else 20000
    output = output or sys.stdout
    ex_set = parse_ex(ex)
    if len(ex_set) > 0:
        conf['ex'] = ex_set
    else:
        ex = '_'
    run_results = []
    adv, real_d = run_once(classname, conf, duration, cond)
    if verbose == 1:
        adv.logs.write_logs(output=output)
        act_sum(adv.logs.act_seq, output)
        return
    if verbose == 2:
        output.write(adv._acl_str)
        return

    if mass:
        adv.logs, real_d = run_mass(mass, adv.logs, real_d, classname, conf, duration, cond)

    run_results.append((adv, real_d, True))
    no_cond_dps = None
    if adv.condition.exist():
        adv_2, real_d_2 = run_once(classname, conf, duration, False)
        # if mass:
        #     adv_2.logs, real_d_2 = run_mass(mass, adv_2.logs, real_d, classname, conf, duration, False)
        run_results.append((adv_2, real_d_2, False))
        no_cond_dps = {
            'dps': round(dps_sum(real_d_2, adv_2.logs.damage)['dps']),
            'team_buff': adv_2.logs.team_buff / real_d,
            'team_tension': adv_2.logs.team_tension
        }

    if verbose == -5:
        ex_mod_func, ex = build_exp_mod_list(ex, ex_set, adv.conf.c.wt)
        page = 'sp' if special else str(duration)
        for ex_str, mod_func in ex_mod_func:
            output.write('-,{},{}{}\n'.format(page, ex_str, ex))
            for a, d, c in run_results:
                report(d, a, output, team_dps, cond=c, mod_func=mod_func)
    else:
        for a, d, c in run_results:
            if verbose == -2 or verbose == -3:
                if c:
                    output.write('-,{},{}\n'.format(duration, ex))
                report(d, a, output, team_dps, cond=c)
            else:
                summation(d, a, output, cond=c, no_cond_dps=no_cond_dps)

    return run_results

def amulets(adv):
    amulets = '['+adv.slots.a.__class__.__name__ + '+' + adv.slots.a.a2.__class__.__name__+']'
    amulets += '['+adv.slots.d.__class__.__name__+']'
    amulets += '['+adv.slots.w.__class__.__name__.split('_')[0]+']'
    return amulets

def append_condensed(condensed, act):
    if len(condensed) > 0:
        l_act, l_cnt = condensed[-1]
        if l_act == act:
            condensed[-1] = (l_act, l_cnt+1)
            return condensed
    condensed.append((act, 1))
    return condensed

def act_repeats(condensed):
    from collections import Counter
    condensed = list(filter(lambda a: a[0] != 'dshift', condensed))
    start = 0
    maxlen = len(condensed)
    bestest = condensed, 1, 0
    for start in range(0, maxlen):
        accumulator = Counter()
        length = 1
        c_slice = tuple(condensed[start:start+length])
        while start+length*(accumulator[c_slice]+1) <= maxlen:
            n_slice = tuple(condensed[start+length*accumulator[c_slice]:start+length*(accumulator[c_slice]+1)])
            if n_slice == c_slice:
                accumulator[c_slice] += 1
            else:
                length += 1
                c_slice = tuple(condensed[start:start+length])
                accumulator[c_slice] = 1
        c_best = accumulator.most_common(1)
        if len(c_best) > 0 and c_best[0][1] > bestest[1]:
            bestest = (*c_best[0], start)
    return bestest

def act_sum(actions, output):
    p_act = '_'
    p_xseq = 0
    condensed = []
    for act in actions:
        if act[0] == 'x':
            xseq = int(act[1:])
            if xseq < p_xseq:
                condensed = append_condensed(condensed, p_act)
            p_xseq = xseq
        elif act == 'fs' and p_act[0] == 'x':
            p_xseq = 0
            condensed = append_condensed(condensed, p_act+act)
        else:
            if p_act[0] == 'x':
                condensed = append_condensed(condensed, p_act)
            p_xseq = 0
            condensed = append_condensed(condensed, act)
        p_act = act
    if p_act[0] == 'x':
        condensed = append_condensed(condensed, p_act)
    seq, freq, start = act_repeats(condensed)
    seqlen = len(seq)
    if freq < 2 or freq*seqlen < len(condensed) // 4:
        seqlen = 24
        freq = len(condensed) // seqlen
        start = 0
    p_type = None
    idx_offset = 0
    for idx, ac in enumerate(condensed):
        act, cnt = ac
        idx = idx - idx_offset
        if start > idx > 0 and idx % 24 == 0:
            output.write('\n')
        elif freq >= 0 and start < idx and (idx-start) % seqlen == 0:
            output.write('\n')
            freq -= 1
        elif idx > 0:
            output.write(' ')
        if act[0] == 'x' or act == 'fs':
            output.write(act.replace('x', 'c'))
            p_type = 'x'
        else:
            if act == 'dshift':
                output.write('[--- dragon ---]')
                p_type == 'd'
                idx_offset += 1
            else:
                output.write('['+act+']')
                p_type = 's'
        if cnt > 1:
            output.write('*{}'.format(cnt))

def dps_sum(real_d, damage, mod_func=None):
    res = {'dps':0}
    for k, v in damage.items():
        ds = dict_sum(v, mod_func)
        res[k] = ds / real_d
        res['dps'] += ds
    res['dps'] = res['dps'] / real_d
    return res

def dict_sum(sub, mod_func=None):
    if callable(mod_func):
        return sum([mod_func(k2, v2) for k2, v2 in sub.items()])
    else:
        return sum(sub.values())

def damage_counts(real_d, damage, counts, output, mod_func=None, res=None):
    if res is None:
        res = dps_sum(real_d, damage, mod_func)
    if callable(mod_func):
        mod_func = lambda k, v: round(mod_func(k, v))
    else:
        mod_func = lambda k, v: round(v)
    for k1, v1 in damage.items():
        found_count = set()
        if len(v1) > 0 or len(counts[k1]) > 0:
            output.write('\n{:>1} {:>3.0f}%| '.format(k1, res[k1] * 100 / res['dps']))
        for k2, v2 in v1.items():
            modded_value = mod_func(k2, v2)
            try:
                output.write('{}: {:d} [{}], '.format(k2, modded_value, counts[k1][k2]))
                found_count.add(k2)
            except:
                output.write('{}: {:d}, '.format(k2, modded_value))
        for k2, v2 in counts[k1].items():
            if not k2 in found_count:
                output.write('{}: 0 [{}], '.format(k2, counts[k1][k2]))

def summation(real_d, adv, output, cond=True, mod_func=None, no_cond_dps=None):
    res = dps_sum(real_d, adv.logs.damage, mod_func)
    if cond:
        output.write('='*BR+'\n')
        output.write('DPS - {}'.format(round(res['dps'])))
        t_buff = adv.logs.team_buff / real_d
        if t_buff > 0:
            output.write(' (team: {:.2f})'.format(t_buff))
        for k, v in adv.logs.team_tension.items():
            output.write(' ({}: {})'.format(k, int(v)))
        if no_cond_dps:
            output.write(' | {}'.format(no_cond_dps['dps']))
            if no_cond_dps['team_buff'] > 0:
                output.write(' (team: {:.2f})'.format(no_cond_dps['team_buff']))
            for k, v in no_cond_dps['team_tension'].items():
                output.write(' ({}: {})'.format(k, int(v)))
        output.write(', duration {:.2f}s'.format(real_d))

        output.write('\n')
        output.write(adv.__class__.__name__)
        output.write(' ')
        if len(adv.slots.c.ex.keys()) > 0:
            output.write('(')
            output.write(' '.join(adv.slots.c.ex.keys()))
            output.write(') ')
        output.write(amulets(adv))
        output.write('\n')
        cond_comment = []
        if adv.condition.exist():
            cond_comment.append('<{}>'.format(adv.condition.cond_str()))
        if len(adv.comment) > 0:
            cond_comment.append(adv.comment)
        if len(cond_comment) > 0:
            output.write(' '.join(cond_comment))
            output.write('\n')
    output.write('-'*BR)
    damage_counts(real_d, adv.logs.damage, adv.logs.counts, output, mod_func=mod_func, res=res)
    if cond:
        output.write('\n')

def report(real_d, adv, output, team_dps, cond=True, mod_func=None):
    name = adv.__class__.__name__
    condition = '<{}>'.format(adv.condition.cond_str())
    dmg = adv.logs.damage
    res = dps_sum(real_d, dmg, mod_func)
    buff = adv.logs.team_buff / real_d
    report_csv = [res['dps']]
    report_csv.extend([
        name if cond else '_c_'+name,
        adv.conf['c.stars']+'*',
        adv.conf['c.ele'],
        adv.conf['c.wt'],
        adv.displayed_att,
        amulets(adv),
        condition if cond else '!' + condition,
        adv.comment
    ])
    dps_mappings = {}
    dps_mappings['attack'] = dict_sum(dmg['x'], mod_func) / real_d
    for k in sorted(dmg['f']):
        if k == 'fs':
            dps_mappings['force_strike'] = dmg['f']['fs'] / real_d
        else:
            dps_mappings[k] = dmg['f'][k] / real_d
    for k in sorted(dmg['s']):
        if k in ('s1', 's2', 's3'):
            dps_mappings['skill_{}'.format(k[1])] = dmg['s'][k] / real_d
        else:
            dps_mappings[k] = dmg['s'][k] / real_d
    if buff > 0:
        dps_mappings['team_buff'] = buff*team_dps
        report_csv[0] += dps_mappings['team_buff']
    for tension, count in adv.logs.team_tension.items():
        dmg_val = count*skill_efficiency(real_d, team_dps, tension_efficiency[tension])
        if dmg_val > 0:
            dps_mappings['team_{}'.format(tension)] = dmg_val
            report_csv[0] += dmg_val
    for k in sorted(dmg['o']):
        dmg_val = dmg['o'][k]
        if dmg_val > 0:
            dps_mappings[k] = dmg_val / real_d
    for k in sorted(dmg['d'], reverse=True):
        dmg_val = dmg['d'][k]
        if dmg_val > 0:
            if k.startswith('dx') or k == 'dshift':
                k = 'dx'
            try:
                dps_mappings[k] += dmg_val / real_d
            except:
                dps_mappings[k] = dmg_val / real_d

    report_csv[0] = round(report_csv[0])
    if callable(mod_func):
        report_csv.extend(['{}:{}'.format(k, int(mod_func(k, v))) for k, v in dps_mappings.items()])
    else:
        report_csv.extend(['{}:{}'.format(k, int(v)) for k, v in dps_mappings.items()])

    output.write(','.join([str(s) for s in report_csv]))
    output.write('\n')
    return report_csv

def load_adv_module(adv_name):
    return getattr(
        __import__('adv.{}'.format(adv_name.lower())),
        adv_name.lower()
    ).module()

def test_with_argv(*argv, conf={}):
    if argv[0] is not None and not isinstance(argv[0], str):
        module = argv[0]
    else:
        try:
            name = os.path.basename(argv[1]).split('.')[0]
            module = load_adv_module(name)
        except:
            name = 'euden'
            module = load_adv_module(name)
    try:
        verbose = int(argv[2])
    except:
        verbose = 0
    try:
        duration = int(argv[3])
    except:
        duration = 180
    try:
        ex = argv[4]
    except:
        ex = '_'
    try:
        mass = int(argv[5])
    except:
        mass = 0
    test(module, conf=conf, verbose=verbose, duration=duration, ex=ex, mass=mass)

if __name__ == '__main__':
    test_with_argv(*sys.argv)