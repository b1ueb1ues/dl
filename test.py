import adv
import wep.wand
from core.log import *
from adv.maribelle import *
from adv.lily import *
from adv.mikoto import *



def sum_dmg():
    l = logget()
    dmg_sum = {'x': [0, 0], 's': 0  }
    sdmg_sum = {'s1':[0, 0], 's2':[0, 0], 's3':[0, 0]}
    for i in l:
        if i[1] == 'dmg':
            #dmg_sum[i[2][0]] += i[3]
            if i[2][0] == 'x':
                dmg_sum['x'][0] += i[3]
            elif i[2] == 's1':
                dmg_sum['s'] += i[3]
                sdmg_sum['s1'][0] += i[3]
            elif i[2] == 's2':
                dmg_sum['s'] += i[3]
                sdmg_sum['s2'][0] += i[3]
            elif i[2] == 's3':
                dmg_sum['s'] += i[3]
                sdmg_sum['s3'][0] += i[3]
        if i[1] == 'cast':
            if i[2] == 's1':
                sdmg_sum['s1'][1] += 1
            elif i[2] == 's2':
                sdmg_sum['s2'][1] += 1
            elif i[2] == 's3':
                sdmg_sum['s3'][1] += 1

    total = dmg_sum['x'][0] + dmg_sum['s']
    dmg_sum['total'] = total
    print dmg_sum
    print sdmg_sum


conf = {}

conf.update( { 
    "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05} 
    } )

conf['al'] = """
    /s1
    /s2
    /s3
"""

Mikoto(conf).run()
#logcat()
print id(logget())


sum_dmg()



al = {
    'sp': [],
    'x5': ['s1','s2','s3'],
    'x4': [],
    'x3': ['s1','s2','s3'],
    'x2': ['s1','s2','s3'],
    'x1': ['s1','s2','s3'],
    's': ['s1','s2','s3'],
    }

conf['al'] = al

Lily(conf).run()
#logcat()
print id(logget())
sum_dmg()

