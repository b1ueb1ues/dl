import slot
from slot import *


class sword5b1(WeaponBase):
    ele = ['flame','water','light']
    wt = 'sword'
    att = 556
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }

class sword5b2(WeaponBase):
    ele = ['wind','shadow']
    wt = 'sword'
    att = 524
    s3 = {
        "dmg"      : 0        ,
        "sp"       : 7316     ,
        "startup"  : 0.15     ,
        "recovery" : 0.9      ,
        }

class swordHMSBane(WeaponBaseHMS):
    wt = 'sword'
    att = 362

class swordHBHBane(WeaponBaseHBH):
    wt = 'sword'
    att = 362

class swordHMCBane(WeaponBaseHMC):
    wt = 'sword'
    att = 333

class swordHZDBane(WeaponBaseHZD):
    wt = 'sword'
    att = 362

class swordHJPBane(WeaponBaseHJP):
    wt = 'sword'
    att = 351

class sword5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        }

flame  = sword5b1
water  = sword5b1
light  = sword5b1

wind   = sword5b2
shadow = sword5b2


class HDT_Crimson(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        } # Crimson Storm
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Absolute_Crimson(WeaponBase):
    ele = ['flame']
    wt = 'sword'
    att = 1530
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6847     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
        } # Infinite Crimson
    a = []
    ability_desc = {}

class HDT_Aqua(WeaponBase):
    ele = ['water']
    wt = 'sword'
    att = 765
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Aqua Storm
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Absolute_Aqua(WeaponBase):
    ele = ['water']
    wt = 'sword'
    att = 1530
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Infinite Aqua
    a = []
    ability_desc = {}

class HDT_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 705
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Tempest Storm
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Absolute_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'sword'
    att = 1411
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Infinite Tempest
    a = []
    ability_desc = {}

class HDT_Lightning(WeaponBase):
    ele = ['light']
    wt = 'sword'
    att = 743
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Lightning Storm
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Absolute_Lightning(WeaponBase):
    ele = ['light']
    wt = 'sword'
    att = 1485
    s3 = {
        "dmg"      : 3*2.48   ,
        "sp"       : 6418     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Infinite Lightning
    a = []
    ability_desc = {}

class HDT_Hex(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 743
    s3 = {} # Hexing Storm
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Absolute_Hex(WeaponBase):
    ele = ['shadow']
    wt = 'sword'
    att = 1485
    s3 = {
        "dmg"      : 5*1.65   ,
        "sp"       : 6163     ,
        "startup"  : 0.1      ,
        "recovery" : 3.1      ,
<<<<<<< HEAD
        } # Infinite Hexes
    a = []
    ability_desc = {}

=======
        }

flame  = sword5d1flame
water  = sword5d1water
wind   = sword5d1wind
light  = sword5d1light
shadow = sword5d1shadow
>>>>>>> 01fc3bdb99a2329a6c009c19b0b265de12e7ca46
