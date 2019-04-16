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

class bladev5flame(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 353
    a = [('k',0.2), ('prep','50%')]


flame  = blade5b1
wind   = blade5b1

water  = blade5b2
light  = blade5b2

shadow = blade5b3
