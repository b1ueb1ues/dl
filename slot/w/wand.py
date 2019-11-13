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

class wand5b10(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'wand'
    att = 454
    s3 = {
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

class wand5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
        }

class wand5d1water(WeaponBase):
    ele = ['water']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
        }

class wand5d1wind(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 788
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
        }

class wand5d1light(WeaponBase):
    ele = ['light']
    wt = 'wand'
    att = 765
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 7881     ,
        "startup"  : 0.1      ,
        "recovery" : 1.78     ,
        }

class wand5d1shadow(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 742
    s3 = {
        "dmg"      : 9.74     ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.75     ,
        }

flame  = wand5d1flame
water  = wand5d1water
wind   = wand5d1wind
light  = wand5d1light
shadow = wand5d1shadow

