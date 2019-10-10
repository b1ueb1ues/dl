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
        "dmg"      : 7.55     ,
        "sp"       : 15205    ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class staffHJPBane(WeaponBaseHJP):
    wt = 'staff'
    att = 317

flame  = staff5b1
water  = staff5b1
wind   = staff5b1

light  = staff5b2
shadow = staff5b2

