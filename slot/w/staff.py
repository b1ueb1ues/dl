import slot
from slot import *


class staff5b1(WeaponBase):
    ele = ['flame','water','wind']
    wt = 'staff'
    att = 528
    s3 = {
        }

class staff5b2(WeaponBase):
    ele = ['light','shadow']
    wt = 'staff'
    att = 513
    s3 = {
        "s3_dmg"      : 7.55     ,
        "s3_sp"       : 15205    ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
        }

flame  = staff5b1
water  = staff5b1
wind   = staff5b1

light  = staff5b2
shadow = staff5b2

