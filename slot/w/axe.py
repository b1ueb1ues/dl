from slot import *
import slot

class axe5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'axe'
    att = 567
    s3 = {
        "buff"     : ['self',0.5, 20, 'crit','dmg'],
        "sp"       : 4711       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    }

class axe5b2(WeaponBase):
    ele = ['water','wind']
    att = 584
    wt = 'axe'
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 9025     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    }

class axeHMSBane(WeaponBaseHMS):
    wt = 'axe'
    att = 380

class axeHBHBane(WeaponBaseHBH):
    wt = 'axe'
    att = 357

class axeHMCBane(WeaponBaseHMC):
    wt = 'axe'
    att = 357

class axeHZDBane(WeaponBaseHZD):
    wt = 'axe'
    att = 357

class axeHJPBane(WeaponBaseHJP):
    wt = 'axe'
    att = 380

flame  = axe5b1
light  = axe5b1
shadow = axe5b1

water  = axe5b2
wind   = axe5b2

class HDT_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 780
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Crimson Passion
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Royal_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1559
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Royal Crimson Passion
    a = []
    ability_desc = {}

class HDT_Mercys_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 756
    s3 = {} # Mercy's Embrace
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Mercys_Azure_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 1512
    s3 = {} # Mercy's Azure Embrace
    a = []
    ability_desc = {}

class HDT_Storms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 756
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Storm's Wisdom
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Glorystorms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 1512
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Glorystorm's Wisdom
    a = []
    ability_desc = {}

class HDT_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 803
    s3 = {} # Thunder's Delight
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Mighty_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 1606
    s3 = {} # Mighty Thunder's Delight
    a = []
    ability_desc = {}

class HDT_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 803
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Darkbite's Curse
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Shadowy_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 1606
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
    } # Shadowy Darkbite's Curse
    a = []
    ability_desc = {}

