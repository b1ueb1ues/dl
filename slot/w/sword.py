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

class swordv5wind(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 333
    a = [('k',0.3), ('prep','50%')]

class sword5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }

class sword5d1water(WeaponBase):
    ele = ['water']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class sword5d1wind(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 705
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class sword5d1light(WeaponBase):
    ele = ['light']
    wt = 'sword'
    att = 743
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class sword5d1shadow(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 743
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6163     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }

flame  = sword5d1flame
water  = sword5d1water
wind   = sword5d1wind
light  = sword5d1light
shadow = sword5d1shadow
