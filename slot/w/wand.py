import slot
from slot import *

class wand5b2p2(WeaponBase):
    ele = ['all']
    wt = 'wand'
    att = 470
    s3 = {
        "dmg"      : 4*2.44   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wand4b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'wand'
    att = 372
    s3 = {
        "dmg"      : 9.84     ,
        "sp"       : 8453     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wand5b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'wand'
    att = 528
    s3 = {
        }

class wand5b2(WeaponBase):
    ele = ['water','light']
    wt = 'wand'
    att = 573
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wandHMSBane(WeaponBaseHMS):
    wt = 'wand'
    att = 351

class wandHBHBane(WeaponBaseHBH):
    wt = 'wand'
    att = 343

class wandHMCBane(WeaponBaseHMC):
    wt = 'wand'
    att = 372

class wandHZDBane(WeaponBaseHZD):
    wt = 'wand'
    att = 351

class wandHJPBane(WeaponBaseHJP):
    wt = 'wand'
    att = 351


flame  = wand5b1
wind   = wand5b1
shadow = wand5b1

water  = wand5b2
light  = wand5b2

