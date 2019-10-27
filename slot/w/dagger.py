import slot
from slot import *

class dagger5b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'dagger'
    att = 545
    s3 = {
        "dmg"      : 6*1.64   ,
        "sp"       : 7323     ,
        "startup"  : 0.1      ,
        "recovery" : 2.5      ,
        }

class dagger5b2(WeaponBase):
    ele = ['water','light']
    wt = 'dagger'
    att = 529
    s3 = {
        "buff"     : ['self',0.4, 5],
        "sp"       : 7103       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
        }

class daggerHMSBane(WeaponBaseHMS):
    wt = 'dagger'
    att = 354

class daggerHBHBane(WeaponBaseHBH):
    wt = 'dagger'
    att = 344

class daggerHMCBane(WeaponBaseHMC):
    wt = 'dagger'
    att = 354

class daggerHZDBane(WeaponBaseHZD):
    wt = 'dagger'
    att = 327

class daggerHJPBane(WeaponBaseHJP):
    wt = 'dagger'
    att = 334


flame  = dagger5b1
wind   = dagger5b1
shadow = dagger5b1

water  = dagger5b2
light  = dagger5b2


class HDT_Crimson_Fang(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 728
    s3 = {} # Savage Crimson
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Flamerulers_Maw(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1455
    s3 = {} # Savage Flameruler
    a = []
    ability_desc = {}

class HDT_Tidal_Fang(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 728
    s3 = {} # Vicious Tides
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Tiderulers_Maw(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 1455
    s3 = {} # Vicious Tideruler
    a = []
    ability_desc = {}

class HDT_Galestorm_Fang(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 691
    s3 = {} # Merciless Galestorm
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Windrulers_Maw(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 1383
    s3 = {} # Merciless Windruler
    a = []
    ability_desc = {}

class HDT_Lightning_Fang(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 706
    s3 = {} # Ferocious Lightning
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Fulminators_Maw(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 1412
    s3 = {} # Ferocious Fulminator
    a = []
    ability_desc = {}

class HDT_Darkened_Fang(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 706
    s3 = {} # Bloodstarved Darkness
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Shaderulers_Maw(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 1412
    s3 = {} # Bloodstarved Shadowruler
    a = []
    ability_desc = {}
