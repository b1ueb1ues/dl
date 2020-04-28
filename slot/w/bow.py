from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Valkyries_Blaze(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 734
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        "hit"      : 3        ,
    } # Valkyrie's Raid
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Valkyries_Fire(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 1468
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        "hit"      : 3        ,
    } # Valkyrie's Heroic Raid
    a = []

class HDT1_Blue_Mercurius(WeaponBase):
    ele = ['water']
    wt = 'bow'
    att = 713
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.38     ,
        "hit"      : 1        ,
    } # Mercurius's Knowledge
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Azure_Mercurius(WeaponBase):
    ele = ['water']
    wt = 'bow'
    att = 1426
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.38     ,
        "hit"      : 1        ,
    } # Mercurius's Transcendant Knowledge
    a = []

class HDT1_Jormungands_Squall(WeaponBase):
    ele = ['wind']
    wt = 'bow'
    att = 713
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
    } # Jormungand's World
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Jormungands_Fury(WeaponBase):
    ele = ['wind']
    wt = 'bow'
    att = 1426
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 2.73     ,
        "hit"      : 3        ,
    } # Jormungand's Boundless World
    a = []

class HDT1_Jupiters_Light(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 677
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.38     ,
        "hit"      : 1        ,
    } # Jupiter's Protection
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Jupiters_Sky(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 1354
    s3 = {
        "dmg"      : 8.54     ,
        "sp"       : 7267     ,
        "startup"  : 0.1      ,
        "recovery" : 2.38     ,
        "hit"      : 1        ,
    } # Jupiter's Celestial Protection
    a = []

class HDT1_Dark_Prophecy(WeaponBase):
    ele = ['shadow']
    wt = 'bow'
    att = 713
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 1.52     ,
        "hit"      : 1        ,
    } # Prophecy's Guidance
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Hellish_Prophecy(WeaponBase):
    ele = ['shadow']
    wt = 'bow'
    att = 1426
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 6750     ,
        "startup"  : 0.1      ,
        "recovery" : 1.52     ,
        "hit"      : 1        ,
    } # Prophecy's Immaculate Guidance
    a = []

class Chimeratech_Bow(WeaponBase):
    ele = ['flame', 'shadow']
    wt = 'bow'
    att = 961
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Ydalir(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 1482
    s3 = agito_buffs['flame'][1]

class Agito0UB_Ydalir(Agito_Ydalir):
    att = 961
    s3 = agito_buffs['flame'][0]

class Agito_Longshe_Gong(WeaponBase):
    ele = ['shadow']
    wt = 'bow'
    att = 1482
    s3 = agito_buffs['shadow'][1]

class Agito0UB_Longshe_Gong(Agito_Longshe_Gong):
    att = 961
    s3 = agito_buffs['shadow'][0]

class Agito_Failnaught(WeaponBase):
    ele = ['wind']
    wt = 'bow'
    att = 1482
    s3 = agito_buffs['wind'][1]

class Agito0UB_Failnaught(Agito_Failnaught):
    att = 961
    s3 = agito_buffs['wind'][0]

class UnreleasedAgitoStr_WaterBow(Agito_Ydalir):
    ele = ['water']

class UnreleasedAgitoStr_LightBow(Agito_Ydalir):
    ele = ['light']

class UnreleasedAgitoSpd_WaterBow(Agito_Longshe_Gong):
    ele = ['water']

class UnreleasedAgitoSpd_LightBow(Agito_Longshe_Gong):
    ele = ['light']

flame = Agito_Ydalir
water = HDT2_Azure_Mercurius
wind = Agito_Failnaught
light = HDT2_Jupiters_Sky
shadow = Agito_Longshe_Gong