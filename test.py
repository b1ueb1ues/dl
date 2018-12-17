import adv
import wep.wand
from core.log import *
from adv.maribelle import *
from adv.lily import *
from adv.mikoto import *


conf = {}

conf.update( { 
    "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05} 
    } )

al = {
    'sp': [],
    'x5': [],
    'x4': [],
    'x3': [],
    'x2': [],
    'x1': [],
    's': [],
    }

al.update( {
    #'sp': ["s1","s2"],
    'x5': ["s1"],
    'x4': ["s1"],
    'x3': ["s1"],
    'x2': ["s1"],
    'x1': ["s1"],
    's': ["s1","s3","s2"],
    } )

conf['al'] = al

def sum_dmg():
    l = logget()
    dmg_sum = {'x': [0, 0], 's': 0  }
    sdmg_sum = {'s1':[0, 0], 's2':[0, 0], 's3':[0, 0]}
    for i in l:
        if i[1] == 'dmg':
            #dmg_sum[i[2][0]] += i[3]
            if i[2][0] == 'x':
                dmg_sum['x'][0] += i[3]
                dmg_sum['x'][1] += 1
            elif i[2] == 's1':
                dmg_sum['s'] += i[3]
                sdmg_sum['s1'][0] += i[3]
                sdmg_sum['s1'][1] += 1
            elif i[2] == 's2':
                dmg_sum['s'] += i[3]
                sdmg_sum['s2'][0] += i[3]
                sdmg_sum['s2'][1] += 1
            elif i[2] == 's3':
                dmg_sum['s'] += i[3]
                sdmg_sum['s3'][0] += i[3]
                sdmg_sum['s3'][1] += 1

    total = dmg_sum['x'][0] + dmg_sum['s']
    dmg_sum['total'] = total
    print dmg_sum
    print sdmg_sum


Mikoto(conf).run()
logcat()
sum_dmg()
exit()

Lily(conf).run()
#logcat()
sum_dmg()

