import io
import os
import inspect
from contextlib import redirect_stdout
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import slot.a
import slot.d
import slot.w

app = Flask(__name__)
CORS(app)

# Helpers
def get_adv_module(adv_name):
    return getattr(
                __import__('adv.{}'.format(adv_name.lower())), 
                adv_name.lower()
           ).module()
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
def list_members(module, predicate, element=None, weapon=None):
    members = inspect.getmembers(module, predicate)
    member_list = []
    for m in members:
        n, c = m

        if weapon is not None:
            if module == slot.w and c.__module__ != 'slot.w.{}'.format(weapon):
                continue
        if element is not None:
            if module == slot.d and c.__module__ != 'slot.d.{}'.format(element):
                continue
            if module == slot.w and element not in getattr(c, 'ele'):
                continue

        fullname = (c.__module__, c.__qualname__)
        if fullname not in member_list:
            member_list.append(fullname)
    return member_list

# API
@app.route('/adv_test', methods=['GET'])
def run_adv_test():
    adv_name = request.args.get('adv', default='euden')
    wp1 = request.args.get('wp1', default=None)
    wp2 = request.args.get('wp2', default=None)
    dra = request.args.get('dra', default=None)
    ex  = request.args.get('ex', default='')
    wep = request.args.get('wep', default=None)
    t   = abs(int(request.args.get('t', default=180)))

    # log = int(request.args.get('log', default=0))
    # if log not in [-2, 0]:
    #     log = 0
    log = -2

    import adv.adv_test
    adv.adv_test.set_ex(ex)
    
    adv_module = get_adv_module(adv_name)
    conf = {}
    def slot_injection(this):
        if wp1 is not None and wp2 is not None:
            this.conf['slots.a'] = getattr(slot.a, wp1)() + getattr(slot.a, wp2)()
        if dra is not None:
            this.conf['slots.d'] = getattr(slot.d, dra)()
        if wep is not None:
            this.conf['slots.w'] = getattr(slot.w, wep)()
    adv_module.slot_backdoor = slot_injection

    f = io.StringIO()
    with redirect_stdout(f):
        adv.adv_test.test(adv_module, conf, verbose=log, duration=t)
    return f.getvalue()


@app.route('/adv_slotlist', methods=['GET'])
def get_adv_slotlist():
    result = {}
    result['amulets'] = list_members(slot.a, is_amulet)
    result['adv_name'] = request.args.get('adv', default=None)
    result['adv_ele'] = None
    result['adv_wt'] = None
    if result['adv_name'] is not None:
        adv_instance = get_adv_module(result['adv_name'])()
        result['adv_ele'] = adv_instance.slots.c.ele.lower()
        result['adv_wt'] = adv_instance.slots.c.wt.lower()
    result['dragons'] = list_members(slot.d, is_dragon, element=result['adv_ele'], weapon=result['adv_wt'])
    result['weapons'] = list_members(slot.w, is_weapon, element=result['adv_ele'], weapon=result['adv_wt'])
    return jsonify(result)