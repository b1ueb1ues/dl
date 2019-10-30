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
        "recovery" : 2.25     ,
    }

class axe5d1wind(WeaponBase):
    ele = ['wind']
    att = 756
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    }

class axe5d1shadow(WeaponBase):
    ele = ['shadow']
    att = 803
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    }

flame  = axe5b1
light  = axe5b1
shadow = axe5b1

water  = axe5b2
wind   = axe5b2

