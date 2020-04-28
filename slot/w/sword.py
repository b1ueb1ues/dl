from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Crimson(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        "hit"      : 5        ,
    } # Crimson Storm
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Absolute_Crimson(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 1530
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        "hit"      : 5        ,
    } # Infinite Crimson
    a = []

class HDT1_Aqua(WeaponBase):
    ele = ['water']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Aqua Storm
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Absolute_Aqua(WeaponBase):
    ele = ['water']
    wt = 'sword'
    att = 1530
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Infinite Aqua
    a = []

class HDT1_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 705
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Tempest Storm
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Absolute_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 1411
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Infinite Tempest
    a = []

class HDT1_Lightning(WeaponBase):
    ele = ['light']
    wt = 'sword'
    att = 743
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Lightning Storm
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Absolute_Lightning(WeaponBase):
    ele = ['light']
    wt = 'sword'
    att = 1485
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        "hit"      : 3        ,
    } # Infinite Lightning
    a = []

class HDT1_Hex(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 743
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6163     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        "hit"      : 5        ,
    } # Hexing Storm
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Absolute_Hex(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 1485
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6163     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        "hit"      : 5        ,
    } # Infinite Hexes
    a = []

class Chimeratech_Sword(WeaponBase):
    ele = ['flame', 'shadow']
    wt = 'sword'
    att = 972
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Nothung(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 1544
    s3 = agito_buffs['flame'][1]

class Agito0UB_Nothung(Agito_Nothung):
    att = 1001
    s3 = agito_buffs['flame'][0]

class Agito_Yitian_Jian(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 1544
    s3 = agito_buffs['shadow'][1]

class Agito0UB_Yitian_Jian(Agito_Yitian_Jian):
    att = 1001
    s3 = agito_buffs['shadow'][0]

class Agito_Excalibur(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 1544
    s3 = agito_buffs['wind'][1]

class Agito0UB_Excalibur(Agito_Excalibur):
    att = 1001
    s3 = agito_buffs['wind'][0]

class UnreleasedAgitoStr_WaterSword(Agito_Nothung):
    ele = ['water']

class UnreleasedAgitoStr_LightSword(Agito_Nothung):
    ele = ['light']

class UnreleasedAgitoSpd_WaterSword(Agito_Yitian_Jian):
    ele = ['water']

class UnreleasedAgitoSpd_LightSword(Agito_Yitian_Jian):
    ele = ['light']

flame = Agito_Nothung
water = HDT2_Absolute_Aqua
wind = Agito_Excalibur
light = HDT2_Absolute_Lightning
shadow = Agito_Yitian_Jian