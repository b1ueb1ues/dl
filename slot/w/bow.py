from slot import *

class Valkyries_Blaze(WeaponBase):
    ele = 'flame'
    wt = 'bow'
    att = 734
    s3 = {} # Valkyrie's Raid
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Valkyries_Fire(WeaponBase):
    ele = 'flame'
    wt = 'bow'
    att = 1468
    s3 = {} # Valkyrie's Heroic Raid
    a = []
    ability_desc = {}

class Blue_Mercurius(WeaponBase):
    ele = 'water'
    wt = 'bow'
    att = 713
    s3 = {} # Mercurius's Knowledge
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Azure_Mercurius(WeaponBase):
    ele = 'water'
    wt = 'bow'
    att = 1426
    s3 = {} # Mercurius's Transcendant Knowledge
    a = []
    ability_desc = {}

class Jormungands_Squall(WeaponBase):
    ele = 'wind'
    wt = 'bow'
    att = 713
    s3 = {} # Jormungand's World
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Jormungands_Fury(WeaponBase):
    ele = 'wind'
    wt = 'bow'
    att = 1426
    s3 = {} # Jormungand's Boundless World
    a = []
    ability_desc = {}

class Jupiters_Light(WeaponBase):
    ele = 'light'
    wt = 'bow'
    att = 677
    s3 = {} # Jupiter's Protection
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Jupiters_Sky(WeaponBase):
    ele = 'light'
    wt = 'bow'
    att = 1354
    s3 = {} # Jupiter's Celestial Protection
    a = []
    ability_desc = {}

class Dark_Prophecy(WeaponBase):
    ele = 'shadow'
    wt = 'bow'
    att = 713
    s3 = {} # Prophecy's Guidance
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Hellish_Prophecy(WeaponBase):
    ele = 'shadow'
    wt = 'bow'
    att = 1426
    s3 = {} # Prophecy's Immaculate Guidance
    a = []
    ability_desc = {}


flame = Valkyries_Fire
water = Azure_Mercurius
wind = Jormungands_Fury
light = Jupiters_Sky
shadow = Hellish_Prophecy