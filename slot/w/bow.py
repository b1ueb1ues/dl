from slot import *


class bow5b1(WeaponBase):
    ele = ['flame','water','wind']
    wt = 'bow'
    att = 518
    s3 = {
        "s3_buff"     : ['self',0.25, 10, 'crit','chance'] ,
        "s3_sp"       : 7316          ,
        "s3_startup"  : 0.10+0.15     ,
        "s3_recovery" : 1.05-0.15     ,
        }

class bow5b2(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 534
    s3 = {
        "s3_dmg"      : 9.49     ,
        "s3_sp"       : 8075     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.25     ,
        }


class bow5b3(WeaponBase):
    ele = ['shadow']
    att = 534
    wt = 'bow'
    s3 = {
        "s3_dmg"      : 3*3.16   ,
        "s3_sp"       : 7501     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.75     ,
        }

flame  = bow5b1
water  = bow5b1
wind   = bow5b1

light  = bow5b2

shadow = bow5b3
