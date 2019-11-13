import slot
from slot import *


class lance5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'lance'
    att = 567
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 8111     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class lance5b2(WeaponBase):
    ele = ['water','wind']
    wt = 'lance'
    att = 523
    s3 = {
        }

class lance5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class lance5d1water(WeaponBase):
    ele = ['water']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        }

class lance5d1wind(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 757
    s3 = {
        "dmg"      : 10*0.92  ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.55     ,
        }

class lance5d1light(WeaponBase):
    ele = ['light']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        }

class lance5d1shadow(WeaponBase):
    ele = ['shadow']
    wt = 'lance'
    att = 719
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

flame  = lance5d1flame
water  = lance5d1water
wind   = lance5d1wind
light  = lance5d1light
shadow = lance5d1shadow
