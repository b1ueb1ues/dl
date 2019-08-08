import types
import importlib.machinery
import io
import os
from contextlib import redirect_stdout
from flask import Flask
from flask import request
app = Flask(__name__)

PATH = "D:\\Desktop\\degenlost\\dl\\adv"

@app.route('/advtest', methods=['GET'])
def adv_test_api():
    if request.method == 'GET':
        adv_name = request.args.get('name', default='xander')
        wp1 = request.args.get('wp1', default=None)
        wp2 = request.args.get('wp2', default=None)
        dra = request.args.get('dra', default=None)
        verbose = int(request.args.get('verbose', default=0))

        import adv.adv_test
        import slot.a
        import slot.d
        # TODO: figure out how to implement bane weaps and arbiturary dragons/wps
        # import slot.w

        adv_module_path = os.path.join(PATH, adv_name.lower() + '.py')
        loader = importlib.machinery.SourceFileLoader('adventurer', adv_module_path)
        mod = types.ModuleType(loader.name)
        loader.exec_module(mod)
        adv_module = mod.module()
        conf = {}

        def conf_injection(this):
            if wp1 is not None and wp2 is not None:
                this.conf['slots.a'] = getattr(slot.a, wp1)() + getattr(slot.a, wp2)()
            if dra is not None:
                this.conf['slots.d'] = getattr(slot.d, dra)()
        adv_module.slot_backdoor = conf_injection

        f = io.StringIO()
        with redirect_stdout(f):
            adv.adv_test.test(adv_module, conf, verbose=verbose)
        return f.getvalue()
    else:
        return 'Bad Request'