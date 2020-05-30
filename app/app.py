import io
import inspect
from importlib.util import spec_from_file_location, module_from_spec
import os
import sys

from contextlib import redirect_stdout
from flask import Flask
from flask import request
from flask import jsonify

import core.simulate
import slot.a
import slot.d
import slot.w
from core.afflic import AFFLICT_LIST
from conf import coability_dict, skillshare
app = Flask(__name__)

# Helpers
ROOT_DIR = os.getenv('ROOT_DIR', '..')
ADV_DIR = 'adv'
MEANS_ADV = {
    'addis': 'addis.py.means.py',
    'sazanka': 'sazanka.py.means.py',
    'victor': 'victor.py.means.py'
}

NORMAL_ADV = ['halloween_lowen']
MASS_SIM_ADV = []

with open(os.path.join(ROOT_DIR, 'chara_quick.txt')) as f:
    for l in f:
        NORMAL_ADV.append(l.strip().replace('.py', ''))

with open(os.path.join(ROOT_DIR, 'chara_slow.txt')) as f:
    for l in f:
        MASS_SIM_ADV.append(l.strip().replace('.py', ''))

SPECIAL_ADV = {
    'chelsea_rollfs': {
        'fn': 'chelsea.py.rollfs.py',
        'nc': ['wp', 'coab']
    },
    'gala_luca_maxstacks': {
        'fn': 'gala_luca.py.maxstacks.py',
        'nc': []
    },
    'veronica_1hp': {
        'fn': 'veronica.py.1hp.py',
        'nc': []
    },
    'natalie_1hp': {
        'fn': 'natalie.py.1hp.py',
        'nc': []
    },
    'valentines_addis_1hp': {
        'fn': 'valentines_addis.py.1hp.py',
        'nc': []
    },
    'bellina_1hp': {
        'fn': 'bellina.py.1hp.py',
        'nc': []
    },
    'fjorm_stack': {
        'fn': 'fjorm.py.x4.py',
        'nc': ['acl']
    }
}

def get_adv_module(adv_name):
    if adv_name in SPECIAL_ADV or adv_name in MEANS_ADV:
        if adv_name in MEANS_ADV:
            adv_file = MEANS_ADV[adv_name]
        else:
            adv_file = SPECIAL_ADV[adv_name]['fn']
        fn = os.path.join(ROOT_DIR, ADV_DIR, adv_file)
        spec = spec_from_file_location(adv_name, fn)
        module = module_from_spec(spec)
        sys.modules[adv_name] = module
        spec.loader.exec_module(module)
        return module.module()
    else:
        return getattr(
            __import__('adv.{}'.format(adv_name.lower())),
            adv_name.lower()
        ).module()

ADV_MODULES = {}
for adv in NORMAL_ADV+MASS_SIM_ADV:
    module = get_adv_module(adv)
    name = module.__name__
    ADV_MODULES[name.lower()] = module
for name, info in SPECIAL_ADV.items():
    module = get_adv_module(name)
    ADV_MODULES[name.lower()] = module

def is_amulet(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.a.Amulet)
            and obj.__module__ != 'slot.a'
            and obj.__module__ != 'slot')
def is_dragon(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.d.DragonBase)
            and obj.__module__ != 'slot.d'
            and obj.__module__ != 'slot')
def is_weapon(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.d.WeaponBase)
            and obj.__module__ != 'slot.w'
            and obj.__module__ != 'slot')
def list_members(module, predicate, element=None):
    members = inspect.getmembers(module, predicate)
    member_list = []
    for m in members:
        _, c = m
        if element is not None:
            if issubclass(c, slot.d.WeaponBase)  and element not in getattr(c, 'ele'):
                continue
        if c.__qualname__ not in member_list:
            member_list.append(c.__qualname__)
    return member_list

def set_teamdps_res(result, logs, real_d, suffix=''):
    result['extra' + suffix] = {}
    if logs.team_buff > 0:
        result['extra' + suffix]['team_buff'] = '+{}%'.format(round(logs.team_buff / real_d * 100))
    for tension, count in logs.team_tension.items():
        if count > 0:
            result['extra' + suffix]['team_{}'.format(tension)] = '{} stacks'.format(round(count))
    return result

def run_adv_test(adv_name, wp1=None, wp2=None, dra=None, wep=None, acl=None, conf=None, cond=None, teamdps=None, t=180, log=-2, mass=0):
    adv_module = ADV_MODULES[adv_name.lower()]
    def acl_injection(self):
        if acl is not None:
            self.conf['acl'] = acl
    adv_module.acl_backdoor = acl_injection
    if conf is None:
        conf = {}

    conf['slots.forced'] = True
    if wp1 is not None and wp2 is not None:
        conf['slots.a'] = getattr(slot.a, wp1)() + getattr(slot.a, wp2)()
    if dra is not None:
        conf['slots.d'] = getattr(slot.d, dra)()
    if wep is not None:
        conf['slots.w'] = getattr(slot.w, wep)()

    result = {}

    fn = io.StringIO()
    try:
        run_res = core.simulate.test(adv_module, conf, t, log, mass, output=fn, team_dps=teamdps, cond=cond)
        result['test_output'] = fn.getvalue()
    except Exception as e:
        result['error'] = str(e)
        return result

    result['logs'] = {}
    adv = run_res[0][0]
    fn = io.StringIO()
    adv.logs.write_logs(output=fn, log_filter=[str(type(adv.slots.d).__name__), str(type(adv).__name__)])
    result['logs']['dragon'] = fn.getvalue()
    fn = io.StringIO()
    core.simulate.act_sum(adv.logs.act_seq, fn)
    result['logs']['action'] = fn.getvalue()
    result['logs']['summation'] = '\n'.join(['{}: {}'.format(k, v) for k, v in adv.logs.counts.items() if v])
    fn = io.StringIO()
    adv.logs.write_logs(output=fn)
    result['logs']['timeline'] = fn.getvalue()
    result = set_teamdps_res(result, adv.logs, run_res[0][1])
    if adv.condition.exist():
        result['condition'] = dict(adv.condition)
        adv_2 = run_res[1][0]
        result = set_teamdps_res(result, adv_2.logs, run_res[0][1], '_no_cond')
    return result

# API
@app.route('/simc_adv_test', methods=['POST'])
def simc_adv_test():
    if not request.method == 'POST':
        return 'Wrong request method.'
    params = request.get_json(silent=True)
    adv_name = 'euden' if not 'adv' in params or params['adv'] is None else params['adv'].lower()
    wp1 = params['wp1'] if 'wp1' in params else None
    wp2 = params['wp2'] if 'wp2' in params else None
    dra = params['dra'] if 'dra' in params else None
    wep = params['wep'] if 'wep' in params else None
    # ex  = params['ex'] if 'ex' in params else ''
    acl = params['acl'] if 'acl' in params else None
    cond = params['condition'] if 'condition' in params and params['condition'] != {} else None
    teamdps = None if not 'teamdps' in params else abs(float(params['teamdps']))
    t   = 180 if not 't' in params else abs(float(params['t']))
    log = -2
    mass = 25 if adv_name in MASS_SIM_ADV and adv_name not in MEANS_ADV else 0
    coab = None if 'coab' not in params else params['coab']
    share = None if 'share' not in params else params['share']
    # latency = 0 if 'latency' not in params else abs(float(params['latency']))
    print(params, flush=True)

    if adv_name in SPECIAL_ADV:
        not_customizable = SPECIAL_ADV[adv_name]['nc']
        if 'wp' in not_customizable:
            wp1 = None
            wp2 = None
        if 'acl' in not_customizable:
            acl = None
        if 'coab' in not_customizable:
            coab = None

    conf = {}
    if 'missile' in params:
        missile = abs(float(params['missile']))
        if missile > 0:
            conf['missile_iv'] = {'fs': missile, 'x1': missile, 'x2': missile, 'x3': missile, 'x4': missile, 'x5': missile}
    if coab is not None:
        conf['coabs'] = coab
    if share is not None:
        conf['skill_share'] = share
    for afflic in AFFLICT_LIST:
        try:
            conf['afflict_res.'+afflic] = min(abs(int(params['afflict_res'][afflic])), 100)
        except:
            pass
    try:
        if params['sim_afflict_type'] in ['burn', 'paralysis', 'poison', 'frostbite']:
            conf['sim_afflict.efficiency'] = abs(float(params['sim_afflict_time'])) / 100
            conf['sim_afflict.type'] = params['sim_afflict_type']
    except:
        pass
    try:
        conf['sim_buffbot.buff'] = min(max(int(params['sim_buff_str']), -1000), 1000)/100
    except:
        pass
    try:
        conf['sim_buffbot.debuff'] = min(max(int(params['sim_buff_def']), -50), 50)/100
    except:
        pass

    result = run_adv_test(adv_name, wp1, wp2, dra, wep, acl, conf, cond, teamdps, t=t, log=log, mass=mass)
    return jsonify(result)

@app.route('/simc_adv_slotlist', methods=['GET', 'POST'])
def get_adv_slotlist():
    result = {}
    result['adv'] = {}
    if request.method == 'GET':
        result['adv']['name'] = request.args.get('adv', default=None)
    elif request.method == 'POST':
        params = request.get_json(silent=True)
        result['adv']['name'] = params['adv'].lower() if 'adv' in params else None
    else:
        return 'Wrong request method.'
    adv_ele = None
    dragon_module = slot.d
    weap_module = slot.w
    if result['adv']['name'] is not None:
        adv_instance = ADV_MODULES[result['adv']['name'].lower()]()
        adv_ele = adv_instance.slots.c.ele.lower()
        result['adv']['fullname'] = adv_instance.__class__.__name__
        result['adv']['ele'] = adv_ele
        dragon_module = getattr(slot.d, adv_ele)
        result['adv']['wt'] = adv_instance.slots.c.wt.lower()
        weap_module = getattr(slot.w, result['adv']['wt'])
        result['coab'] = coability_dict(adv_ele)
        result['adv']['pref_dra'] = type(adv_instance.slots.d).__qualname__
        result['adv']['pref_wep'] = type(adv_instance.slots.w).__qualname__
        result['adv']['pref_wp'] = {
            'wp1': type(adv_instance.slots.a).__qualname__,
            'wp2': type(adv_instance.slots.a.a2).__qualname__
        }
        result['adv']['pref_coab'] = adv_instance.coab
        result['adv']['pref_share'] = adv_instance.share
        result['adv']['acl'] = adv_instance.conf.acl
        if 'afflict_res' in adv_instance.conf:
            res_conf = adv_instance.conf.afflict_res
            res_dict = {}
            for afflic in AFFLICT_LIST:
                if afflic in res_conf:
                    res_dict[afflic] = res_conf[afflic]
            if len(res_dict.keys()) > 0:
                result['adv']['afflict_res'] = res_dict
        if result['adv']['name'] in SPECIAL_ADV:
            result['adv']['no_config'] = SPECIAL_ADV[result['adv']['name']]['nc']
    # result['amulets'] = list_members(slot.a, is_amulet)
    result['dragons'] = list_members(dragon_module, is_dragon, element=adv_ele)
    result['weapons'] = list_members(weap_module, is_weapon, element=adv_ele)
    return jsonify(result)


@app.route('/simc_adv_wp_list', methods=['GET', 'POST'])
def get_adv_wp_list():
    if not (request.method == 'GET' or request.method == 'POST'):
        return 'Wrong request method.'
    result = {}
    result['amulets'] = list_members(slot.a, is_amulet)
    result['adv'] = list(ADV_MODULES.keys())
    result['skillshare'] = dict(sorted(skillshare.items()))
    return jsonify(result)