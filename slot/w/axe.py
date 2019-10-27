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

class axeHMSBane(WeaponBaseHMS):
    wt = 'axe'
    att = 380

class axeHBHBane(WeaponBaseHBH):
    wt = 'axe'
    att = 357

class axeHMCBane(WeaponBaseHMC):
    wt = 'axe'
    att = 357

class axeHZDBane(WeaponBaseHZD):
    wt = 'axe'
    att = 357

class axeHJPBane(WeaponBaseHJP):
    wt = 'axe'
    att = 380

flame  = axe5b1
light  = axe5b1
shadow = axe5b1

water  = axe5b2
wind   = axe5b2

