import slot
from slot import *


class blade5b1(WeaponBase):
    ele = ['flame','wind']
    wt = 'blade'
    att = 572
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 8030     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    }

class blade5b2(WeaponBase):
    ele = ['water','light']
    wt = 'blade'
    att = 544

class blade5b3(WeaponBase):
    ele = ['shadow']
    att = 590
    wt = 'blade'
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 7695   ,
        "startup"  : 0.1    ,
        "recovery" : 2.65   ,
    }

class blade4b2(WeaponBase):
    ele = ['light', 'water']
    att = 382
    wt = 'blade'
    s3 = {
        "dmg"      : 9.66   ,
        "sp"       : 8178   ,
        "startup"  : 0.1    ,
        "recovery" : 1.95   ,
    }

class bladeHMSBane(WeaponBaseHMS):
    wt = 'blade'
    att = 353

class bladeHBHBane(WeaponBaseHBH):
    wt = 'blade'
    att = 361

class bladeHMCBane(WeaponBaseHMC):
    wt = 'blade'
    att = 372

class bladeHZDBane(WeaponBaseHZD):
    wt = 'blade'
    att = 383

class bladeHJPBane(WeaponBaseHJP):
    wt = 'blade'
    att = 383


flame  = blade5b1
wind   = blade5b1

water  = blade5b2
light  = blade5b2

shadow = blade5b3
