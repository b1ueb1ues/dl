import slot
from slot import *


class lance5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'lance'
    att = 567
    s3 = {
        "s3_dmg"      : 2*4.61   ,
        "s3_sp"       : 8111     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
        }

class lance5b2(WeaponBase):
    ele = ['water','wind']
    wt = 'lance'
    att = 523
    s3 = {
        }


flame  = lance5b1
light  = lance5b1
shadow = lance5b1

water  = lance5b2
wind   = lance5b2


