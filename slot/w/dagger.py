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

class daggerHMSBane(WeaponBaseHMS):
    wt = 'dagger'
    att = 354

class daggerHBHBane(WeaponBaseHBH):
    wt = 'dagger'
    att = 344

class daggerHMCBane(WeaponBaseHMC):
    wt = 'dagger'
    att = 354

class daggerHZDBane(WeaponBaseHZD):
    wt = 'dagger'
    att = 327

class daggerHJPBane(WeaponBaseHJP):
    wt = 'dagger'
    att = 334


flame  = dagger5b1
wind   = dagger5b1
shadow = dagger5b1

water  = dagger5b2
light  = dagger5b2
