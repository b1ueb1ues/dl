import slot
from slot import *

class dagger5b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'dagger'
    att = 545
    s3 = {
        "s3_dmg"      : 6*1.64   ,
        "s3_sp"       : 7323     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.5      ,
        }

class dagger5b2(WeaponBase):
    ele = ['water','light']
    wt = 'dagger'
    att = 529
    s3 = {
        "s3_buff"     : ['self',0.4, 5],
        "s3_sp"       : 7103       ,
        "s3_startup"  : 0.10+0.15  ,
        "s3_recovery" : 1.05-0.15  ,
        }



flame  = dagger5b1
wind   = dagger5b1
shadow = dagger5b1

water  = dagger5b2
light  = dagger5b2
