from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Crimson_Fang(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Savage Crimson
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Flamerulers_Maw(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1455
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Savage Flameruler
    a = []

class HDT1_Tidal_Fang(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Vicious Tides
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Tiderulers_Maw(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 1455
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Vicious Tideruler
    a = []

class HDT1_Galestorm_Fang(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 691
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Merciless Galestorm
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Windrulers_Maw(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 1383
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Merciless Windruler
    a = []

class HDT1_Lightning_Fang(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Ferocious Lightning
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Fulminators_Maw(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 1412
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Ferocious Fulminator
    a = []

class HDT1_Darkened_Fang(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.73*5   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 2.3      ,
        "hit"      : 5        ,
    } # Bloodstarved Darkness
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Shaderulers_Maw(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 1412
    s3 = {
        "dmg"      : 1.73*5   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 2.3      ,
        "hit"      : 5        ,
    } # Bloodstarved Shadowruler
    a = []

class Chimeratech_Dagger(WeaponBase):
    ele = ['flame', 'shadow', 'wind']
    wt = 'dagger'
    att = 981
    s3 = {} #
    a = [('uo', 0.04)]

class Agito2_Hrotti(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1662
    s3 = agito_buffs['flame'][1]

class Agito1_Hrotti(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1513
    s3 = agito_buffs['flame'][1]

class Agito1_Qinghong_Jian(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 1513
    s3 = agito_buffs['shadow'][1]

class Agito1_Carnwennan(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 1513
    s3 = agito_buffs['wind'][1]

class UnreleasedAgitoStr_WaterDagger(Agito2_Hrotti):
    ele = ['water']

class UnreleasedAgitoStr_LightDagger(Agito2_Hrotti):
    ele = ['light']

class UnreleasedAgitoSpd_WaterDagger(Agito1_Qinghong_Jian):
    ele = ['water']

class UnreleasedAgitoSpd_LightDagger(Agito1_Qinghong_Jian):
    ele = ['light']

flame = Agito2_Hrotti
water = HDT2_Tiderulers_Maw
wind = Agito1_Carnwennan
light = HDT2_Fulminators_Maw
shadow = Agito1_Qinghong_Jian
