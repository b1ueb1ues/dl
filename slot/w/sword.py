from slot import *

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

class Chimeratech_Commander(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 972
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Nothung(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 1544
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Nothung(Agito_Nothung):
    att = 1001
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

class UnreleasedAgito_WaterSword(Agito_Nothung):
    ele = ['water']

class UnreleasedAgito_WindSword(Agito_Nothung):
    ele = ['wind']

class UnreleasedAgito_LightSword(Agito_Nothung):
    ele = ['light']

class UnreleasedAgito_ShadowSword(Agito_Nothung):
    ele = ['shadow']

flame = Agito_Nothung
water = HDT2_Absolute_Aqua
wind = HDT2_Absolute_Tempest
light = HDT2_Absolute_Lightning
shadow = HDT2_Absolute_Hex