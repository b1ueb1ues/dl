import adv
import wep.wand
from core.log import *
from adv.maribelle import *
from adv.lily import *
from adv.mikoto import *
from adv.adv_test import *



conf = {}

conf.update( { 
    "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05} 
    } )

conf['acl'] = """
    `s1,seq=5 and cancel
    `s2,seq=5 and cancel
    `s3,seq=5 and cancel
"""

Mikoto(conf).run()
#logcat()
sum_dmg()



conf['acl'] = """
    #if pin=='prep':prep=1\nelse:prep=0
    `s1,seq=5 and cancel or prep
    `s2,seq=5 and cancel
    `s3,seq=5 and cancel or s=1
"""

Lily(conf).run()
#logcat()
sum_dmg()

