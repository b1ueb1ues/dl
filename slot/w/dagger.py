import slot
from slot import *

class dagger5b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'dagger'
    att = 545
    s3 = {
        "dmg"      : 6*1.64   ,
        "sp"       : 7323     ,
        "startup"  : 0.1      ,
        "recovery" : 2.5      ,
        }

class dagger5b2(WeaponBase):
    ele = ['water','light']
    wt = 'dagger'
    att = 529
    s3 = {
        "buff"     : ['self',0.4, 5],
        "sp"       : 7103       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
        }

class dagger5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        }

class dagger5d1water(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        }

class dagger5d1wind(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 691
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        }

class dagger5d1light(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        }

class dagger5d1shadow(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.73*5   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 2.3      ,
        }

flame  = dagger5d1flame
water  = dagger5d1water
wind   = dagger5d1wind
light  = dagger5d1light
shadow = dagger5d1shadow
