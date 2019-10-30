import slot
from slot import *


class lance5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'lance'
    att = 567
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 8111     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class lance5b2(WeaponBase):
    ele = ['water','wind']
    wt = 'lance'
    att = 523
    s3 = {
        }

class lanceHMSBane(WeaponBaseHMS):
    wt = 'lance'
    att = 358

class lanceHBHBane(WeaponBaseHBH):
    wt = 'lance'
    att = 347

class lanceHMCBane(WeaponBaseHMC):
    wt = 'lance'
    att = 347

class lanceHZDBane(WeaponBaseHZD):
    wt = 'lance'
    att = 358

class lanceHJPBane(WeaponBaseHJP):
    wt = 'lance'
    att = 340

flame  = lance5b1
light  = lance5b1
shadow = lance5b1

water  = lance5b2
wind   = lance5b2


class HDT_Crimsonflame_Lance(WeaponBase):
    ele = ['flame']
    wt = 'lance'
    att = 780
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
    } # Crimson Beacon
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Pureflame_Lance(WeaponBase):
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
    ability_desc = {}

class HDT_Limpid_Lance(WeaponBase):
    ele = ['water']
    wt = 'lance'
    att = 780
    s3 = {} # Limpid Petals
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Limpid_Rush(WeaponBase):
    ele = ['water']
    wt = 'lance'
    att = 1560
    s3 = {} # Limpid Shore
    a = []
    ability_desc = {}

class HDT_Promising_Breeze(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 757
    s3 = {} # Sworn Gale
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Guiding_Gale(WeaponBase):
    ele = ['wind']
    wt = 'lance'
    att = 1515
    s3 = {} # Glorious Gale
    a = []
    ability_desc = {}

class HDT_Lightflash(WeaponBase):
    ele = ['light']
    wt = 'lance'
    att = 780
    s3 = {} # Flashing Thunder
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Brilliant_Lightflash(WeaponBase):
    ele = ['light']
    wt = 'lance'
    att = 1560
    s3 = {} # Brilliant Thunder
    a = []
    ability_desc = {}

class HDT_Scourge_Lance(WeaponBase):
    ele = ['shadow']
    wt = 'lance'
    att = 719
    s3 = {
        "dmg"      : 2*4.61   ,
        "sp"       : 7299     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        } # Hazy Hex
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Ebon_Scourge_Lance(WeaponBase):
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
    ability_desc = {}


