import slot
from slot import *


class sword5b1(WeaponBase):
    ele = ['flame','water','light']
    wt = 'sword'
    att = 556
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }

class sword5b2(WeaponBase):
    ele = ['wind','shadow']
    wt = 'sword'
    att = 524
    s3 = {
        "dmg"      : 0        ,
        "sp"       : 7316     ,
        "startup"  : 0.15     ,
        "recovery" : 0.9      ,
        }

class swordHMSBane(WeaponBaseHMS):
    wt = 'sword'
    att = 362

class swordHBHBane(WeaponBaseHBH):
    wt = 'sword'
    att = 362

class swordHMCBane(WeaponBaseHMC):
    wt = 'sword'
    att = 333

class swordHZDBane(WeaponBaseHZD):
    wt = 'sword'
    att = 362

class swordHJPBane(WeaponBaseHJP):
    wt = 'sword'
    att = 351


flame  = sword5b1
water  = sword5b1
light  = sword5b1

wind   = sword5b2
shadow = sword5b2
