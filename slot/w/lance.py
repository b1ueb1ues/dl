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

class lanceHMSBane(WeaponBaseHMS):
    wt = 'lance'
    att = 358

class lanceHBHBane(WeaponBaseHBH):
    wt = 'lance'
    att = 347

class lanceHMCBane(WeaponBaseHMC):
    wt = 'lance'
    att = 347

class lanceHZDBane(WeaponBaseHZD):
    wt = 'lance'
    att = 358

class lanceHJPBane(WeaponBaseHJP):
    wt = 'lance'
    att = 340

flame  = lance5b1
light  = lance5b1
shadow = lance5b1

water  = lance5b2
wind   = lance5b2


