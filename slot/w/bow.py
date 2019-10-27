from slot import *


class bow5b1(WeaponBase):
    ele = ['flame','water','wind']
    wt = 'bow'
    att = 518
    s3 = {
        "buff"     : ['self',0.25, 10, 'crit','chance'] ,
        "sp"       : 7316          ,
        "startup"  : 0.10+0.15     ,
        "recovery" : 1.05-0.15     ,
        }

class bow5b2(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 534
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 8075     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
        }


class bow5b3(WeaponBase):
    ele = ['shadow']
    att = 534
    wt = 'bow'
    s3 = {
        "dmg"      : 3*3.16   ,
        "sp"       : 7501     ,
        "startup"  : 0.1      ,
        "recovery" : 2.75     ,
        }

class bowHMSBane(WeaponBaseHMS):
    wt = 'bow'
    att = 327

class bowHBHBane(WeaponBaseHBH):
    wt = 'bow'
    att = 337

class bowHMCBane(WeaponBaseHMC):
    wt = 'bow'
    att = 337

class bowHZDBane(WeaponBaseHZD):
    wt = 'bow'
    att = 327

class bowHJPBane(WeaponBaseHJP):
    wt = 'bow'
    att = 337

flame  = bow5b1
water  = bow5b1
wind   = bow5b1

light  = bow5b2

shadow = bow5b3


class HDT_Valkyries_Blaze(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 734
    s3 = {} # Valkyrie's Raid
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Valkyries_Fire(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 1468
    s3 = {} # Valkyrie's Heroic Raid
    a = []
    ability_desc = {}

class HDT_Blue_Mercurius(WeaponBase):
    ele = ['water']
    wt = 'bow'
    att = 713
    s3 = {} # Mercurius's Knowledge
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Azure_Mercurius(WeaponBase):
    ele = ['water']
    wt = 'bow'
    att = 1426
    s3 = {} # Mercurius's Transcendant Knowledge
    a = []
    ability_desc = {}

class HDT_Jormungands_Squall(WeaponBase):
    ele = ['wind']
    wt = 'bow'
    att = 713
    s3 = {} # Jormungand's World
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Jormungands_Fury(WeaponBase):
    ele = ['wind']
    wt = 'bow'
    att = 1426
    s3 = {} # Jormungand's Boundless World
    a = []
    ability_desc = {}

class HDT_Jupiters_Light(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 677
    s3 = {} # Jupiter's Protection
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Jupiters_Sky(WeaponBase):
    ele = ['light']
    wt = 'bow'
    att = 1354
    s3 = {} # Jupiter's Celestial Protection
    a = []
    ability_desc = {}

class HDT_Dark_Prophecy(WeaponBase):
    ele = ['shadow']
    wt = 'bow'
    att = 713
    s3 = {} # Prophecy's Guidance
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Hellish_Prophecy(WeaponBase):
    ele = ['shadow']
    wt = 'bow'
    att = 1426
    s3 = {} # Prophecy's Immaculate Guidance
    a = []
    ability_desc = {}

