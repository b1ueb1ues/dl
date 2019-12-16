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

class bow5d1flame(WeaponBase):
    ele = ['flame']
    att = 734
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        }

class bow5d1water(WeaponBase):
    ele = ['water']
    att = 713
    wt = 'bow'
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }

class bow5d1wind(WeaponBase):
    ele = ['wind']
    att = 713
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        }

class bow5d1light(WeaponBase):
    ele = ['light']
    att = 677
    wt = 'bow'
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }
    
class bow5d1shadow(WeaponBase):
    ele = ['shadow']
    att = 713
    wt = 'bow'
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 1.52     ,
        }

class bow5d2flame(WeaponBase):
    ele = ['flame']
    att = 1468
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        }

class bow5d2water(WeaponBase):
    ele = ['water']
    att = 1426
    wt = 'bow'
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }

class bow5d2wind(WeaponBase):
    ele = ['wind']
    att = 1426
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        }

class bow5d2light(WeaponBase):
    ele = ['light']
    att = 1354
    wt = 'bow'
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }
    
class bow5d2shadow(WeaponBase):
    ele = ['shadow']
    att = 1426
    wt = 'bow'
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 1.52     ,
        }

flame  = bow5d2flame
water  = bow5d2water
wind   = bow5d2wind
light  = bow5d2light
shadow = bow5d2shadow
