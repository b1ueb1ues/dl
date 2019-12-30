from slot import *

class HDT1_Crimsonflame_Lance(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
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
    } # Shadowy Hex
    a = []

class Chimeratech_Lancemaster(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 962
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Gungnir(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 1575
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Gungnir(Agito_Gungnir):
    att = 1021
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

flame = HDT2_Pureflame_Lance
water = HDT2_Limpid_Rush
wind = HDT2_Guiding_Gale
light = HDT2_Brilliant_Lightflash
shadow = HDT2_Ebon_Scourge_Lance