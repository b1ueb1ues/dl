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

class bladev5flame(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 353
    a = [('k',0.2), ('prep','50%')]

class blade5d1flame(WeaponBase):
    ele = ['flame']
    att = 811
    wt = 'blade'
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    }

class blade5d1water(WeaponBase):
    ele = ['water']
    att = 763
    wt = 'blade'
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    }

class blade5d1wind(WeaponBase):
    ele = ['wind']
    att = 787
    wt = 'blade'
    s3 = {
        "dmg"      : 9.57   ,
        "sp"       : 7582   ,
        "startup"  : 0.1    ,
        "recovery" : 2.35   ,
    }

class blade5d1light(WeaponBase):
    ele = ['light']
    att = 748
    wt = 'blade'
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    }

class blade5d1shadow(WeaponBase):
    ele = ['shadow']
    att = 811
    wt = 'blade'
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    }

flame  = blade5d1flame
water  = blade5d1water
wind   = blade5d1wind
light  = blade5d1light
shadow = blade5d1shadow
