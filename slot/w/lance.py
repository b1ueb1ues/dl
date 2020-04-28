from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Crimsonflame_Lance(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 2        ,
    } # Crimson Beacon
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Pureflame_Lance(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 1560
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 2        ,
    } # Crimson Wildfire
    a = []

class HDT1_Limpid_Lance(WeaponBase):
    ele = ['water']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        "hit"      : 2        ,
    } # Limpid Petals
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Limpid_Rush(WeaponBase):
    ele = ['water']
    wt = 'lance'
    att = 1560
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        "hit"      : 2        ,
    } # Limpid Shore
    a = []

class HDT1_Promising_Breeze(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 757
    s3 = {
        "dmg"      : 10*0.92  ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.65     ,
        "hit"      : 10       ,
    } # Sworn Gale
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Guiding_Gale(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 1515
    s3 = {
        "dmg"      : 10*0.92  ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.65     ,
        "hit"      : 10       ,
    } # Glorious Gale
    a = []

class HDT1_Lightflash(WeaponBase):
    ele = ['light']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        "hit"      : 2        ,
    } # Flashing Thunder
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Brilliant_Lightflash(WeaponBase):
    ele = ['light']
    wt = 'lance'
    att = 1560
    s3 = {
        "dmg"      : 2*4.14   ,
        "sp"       : 6762     ,
        "startup"  : 0.1      ,
        "recovery" : 3.33     ,
        "hit"      : 2        ,
    } # Brilliant Thunder
    a = []

class HDT1_Scourge_Lance(WeaponBase):
    ele = ['shadow']
    wt = 'lance'
    att = 719
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 2        ,
    } # Hazy Hex
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Ebon_Scourge_Lance(WeaponBase):
    ele = ['shadow']
    wt = 'lance'
    att = 1439
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 2        ,
    } # Shadowy Hex
    a = []

class Chimeratech_Lance(WeaponBase):
    ele = ['flame', 'shadow']
    wt = 'lance'
    att = 962
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Gungnir(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 1575
    s3 = agito_buffs['flame'][1]

class Agito0UB_Gungnir(Agito_Gungnir):
    att = 1021
    s3 = agito_buffs['flame'][0]

class Agito_Qinglong_Yanyuedao(WeaponBase):
    ele = ['shadow']
    wt = 'lance'
    att = 1575
    s3 = agito_buffs['shadow'][1]

class Agito0UB_Qinglong_Yanyuedao(Agito_Qinglong_Yanyuedao):
    att = 1021
    s3 = agito_buffs['shadow'][0]

class Agito_Rhongomyniad(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 1575
    s3 = agito_buffs['wind'][1]

class Agito0UB_Rhongomyniad(Agito_Rhongomyniad):
    att = 1021
    s3 = agito_buffs['wind'][0]

class UnreleasedAgitoStr_WaterLance(Agito_Gungnir):
    ele = ['water']

class UnreleasedAgitoStr_LightLance(Agito_Gungnir):
    ele = ['light']

class UnreleasedAgitoSpd_WaterLance(Agito_Qinglong_Yanyuedao):
    ele = ['water']

class UnreleasedAgitoSpd_LightLance(Agito_Qinglong_Yanyuedao):
    ele = ['light']

flame = Agito_Gungnir
water = HDT2_Limpid_Rush
wind = Agito_Rhongomyniad
light = HDT2_Brilliant_Lightflash
shadow = Agito_Qinglong_Yanyuedao