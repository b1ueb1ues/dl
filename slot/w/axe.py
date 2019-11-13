from slot import *
import slot

class axe5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'axe'
    att = 567
    s3 = {
        "buff"     : ['self',0.5, 20, 'crit','dmg'],
        "sp"       : 4711       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    }

class axe5b2(WeaponBase):
    ele = ['water','wind']
    att = 584
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 9025     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    }

class axev5flame(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 380
    a = [('k',0.2), ('prep','50%')]

class axe5d1flame(WeaponBase):
    ele = ['flame']
    att = 780
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    }

class axe5d1water(WeaponBase):
    ele = ['water']
    att = 756
    wt = 'axe'
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    }

class axe5d1wind(WeaponBase):
    ele = ['wind']
    att = 756
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    }

class axe5d1light(WeaponBase):
    ele = ['light']
    att = 803
    wt = 'axe'
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    }

class axe5d1shadow(WeaponBase):
    ele = ['shadow']
    att = 803
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    }

flame  = axe5d1flame
water  = axe5d1water
wind   = axe5d1wind
light  = axe5d1light
shadow = axe5d1shadow

