from slot import *


class bow5b1(WeaponBase):
    ele = ['flame','water','wind']
    wt = 'bow'
    att = 518
    s3 = {
        "buff"     : ['self',0.25, 10, 'crit','chance'] ,
        "sp"       : 7316          ,
        "startup"  : 0.10+0.15     ,
        "recovery" : 1.05-0.15     ,
        }

class bow5b2(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 534
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 8075     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
        }


class bow5b3(WeaponBase):
    ele = ['shadow']
    att = 534
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 7501     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }

class bowHMSBane(WeaponBaseHMS):
    wt = 'bow'
    att = 327

class bowHBHBane(WeaponBaseHBH):
    wt = 'bow'
    att = 337

class bowHMCBane(WeaponBaseHMC):
    wt = 'bow'
    att = 337

class bowHZDBane(WeaponBaseHZD):
    wt = 'bow'
    att = 327

class bowHJPBane(WeaponBaseHJP):
    wt = 'bow'
    att = 337

flame  = bow5b1
water  = bow5b1
wind   = bow5b1

light  = bow5b2

shadow = bow5b3
