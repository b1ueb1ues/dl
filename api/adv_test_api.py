import io
import os
import inspect
from contextlib import redirect_stdout
from flask import Flask
from flask import request
from flask import jsonify

import slot.a
import slot.d
import slot.w

app = Flask(__name__)

@app.route('/advtest', methods=['GET'])
def run_adv_test():
    if request.method == 'GET':
        adv_name = request.args.get('name')
        if not adv_name:
            return 'No ADV'
        wp1 = request.args.get('wp1', default=None)
        wp2 = request.args.get('wp2', default=None)
        dra = request.args.get('dra', default=None)
        ex  = request.args.get('ex', default='')
        wep = request.args.get('wep', default=None)
        log = int(request.args.get('log', default=0))
        if log not in [-2, 0]:
            log = 0

        import adv.adv_test
        adv.adv_test.set_ex(ex)
        
        adv_module = getattr(__import__('adv.{}'.format(adv_name.lower())), adv_name.lower()).module()
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
            adv.adv_test.test(adv_module, conf, verbose=log)
        return '<pre>' + f.getvalue() + '</pre>';
    else:
        return 'Bad Request'

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
def list_members(module, predicate, alias=False):
    members = inspect.getmembers(module, predicate)
    member_list = []
    for m in members:
        n, c = m
        if alias:
            fullname = (c.__module__, n)
        else:
            fullname = (c.__module__, c.__qualname__)
        if fullname not in member_list:
            member_list.append(fullname)
    return member_list

@app.route('/slotlist')
def slotlist():
    result = {}
    result['amulets'] = list_members(slot.a, is_amulet)
    result['dragons'] = list_members(slot.d, is_dragon)
    result['weapons'] = list_members(slot.w, is_weapon, alias=False)
    return jsonify(result)