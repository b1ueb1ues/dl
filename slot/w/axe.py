from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 780
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Crimson Passion
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Royal_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1559
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Royal Crimson Passion
    a = []

class HDT1_Mercys_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 756
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
        "hit"      : 5        ,
    } # Mercy's Embrace
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Mercys_Azure_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 1512
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
        "hit"      : 5        ,
    } # Mercy's Azure Embrace
    a = []

class HDT1_Storms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 756
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Storm's Wisdom
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Glorystorms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 1512
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Glorystorm's Wisdom
    a = []

class HDT1_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 803
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
        "hit"      : 5        ,
    } # Thunder's Delight
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Mighty_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 1606
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
        "hit"      : 5        ,
    } # Mighty Thunder's Delight
    a = []

class HDT1_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 803
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Darkbite's Curse
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Shadowy_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 1606
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
        "hit"      : 3        ,
    } # Shadowy Darkbite's Curse
    a = []

class Chimeratech_Axe(WeaponBase):
    ele = ['flame', 'shadow', 'wind']
    wt = 'axe'
    att = 1051
    s3 = {} #
    a = [('uo', 0.04)]

class Agito1_Fangtian_Huaji(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 1621
    s3 = agito_buffs['shadow'][1]

class Agito2_Mjolnir(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1781
    s3 = agito_buffs['flame'][1]

class Agito1_Mjolnir(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1621
    s3 = agito_buffs['flame'][1]

class Agito1_Marmyadose(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 1621
    s3 = agito_buffs['wind'][1]

class UnreleasedAgitoStr_WaterAxe(Agito1_Mjolnir):
    ele = ['water']

class UnreleasedAgitoStr_LightAxe(Agito1_Mjolnir):
    ele = ['light']

class UnreleasedAgitoSpd_WaterAxe(Agito1_Fangtian_Huaji):
    ele = ['water']

class UnreleasedAgitoSpd_LightAxe(Agito1_Fangtian_Huaji):
    ele = ['light']

flame = Agito2_Mjolnir
water = HDT2_Mercys_Azure_Tide
wind = Agito1_Marmyadose
light = HDT2_Mighty_Thundercrash
shadow = Agito1_Fangtian_Huaji