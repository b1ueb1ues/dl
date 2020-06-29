import os
import json
from deploy import load_adv_module_normal, ROOT_DIR
import random

ADV_LISTS = ['chara_quick.txt', 'chara_slow.txt']

ADV_CONF = 'conf/advconf.json'

def stat_shared():
    has_shared = {}
    no_shared = []
    for list_file in ADV_LISTS:
        with open(os.path.join(ROOT_DIR, list_file)) as f:
            for adv_file in f:
                adv_file = os.path.basename(adv_file).strip()
                adv_module = load_adv_module_normal(adv_file)
                if adv_module.share:
                    has_shared[adv_file] = adv_module.share
                else:
                    no_shared.append(adv_file)

    print('Has Shared', len(has_shared))
    for item in has_shared.items():
        print(*item)
    print('\nNo Shared', len(no_shared))
    for idx, adv in enumerate(no_shared):
        print(adv, end='\t' if (idx+1) % 5 else '\n')
    

    random.seed(5)
    print('\n\nDo:')
    print('\n'.join(random.sample(no_shared, 10)))

def stat_conf(cond):
    with open(ADV_CONF) as f:
        data = json.load(f)
    for adv, d in data.items():
        if cond(d):
            print(adv.lower()+'.py')

if __name__ == '__main__':
    stat_conf(lambda d: d['c']['ele'] == 'shadow')