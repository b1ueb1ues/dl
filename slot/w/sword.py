from slot import *

class Crimson(WeaponBase):
    ele = 'flame'
    wt = 'sword'
    att = 765
    s3 = {} # Crimson Storm
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Absolute_Crimson(WeaponBase):
    ele = 'flame'
    wt = 'sword'
    att = 1530
    s3 = {} # Infinite Crimson
    a = []
    ability_desc = {}

class Aqua(WeaponBase):
    ele = 'water'
    wt = 'sword'
    att = 765
    s3 = {} # Aqua Storm
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Absolute_Aqua(WeaponBase):
    ele = 'water'
    wt = 'sword'
    att = 1530
    s3 = {} # Infinite Aqua
    a = []
    ability_desc = {}

class Tempest(WeaponBase):
    ele = 'wind'
    wt = 'sword'
    att = 705
    s3 = {} # Tempest Storm
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Absolute_Tempest(WeaponBase):
    ele = 'wind'
    wt = 'sword'
    att = 1411
    s3 = {} # Infinite Tempest
    a = []
    ability_desc = {}

class Lightning(WeaponBase):
    ele = 'light'
    wt = 'sword'
    att = 743
    s3 = {} # Lightning Storm
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Absolute_Lightning(WeaponBase):
    ele = 'light'
    wt = 'sword'
    att = 1485
    s3 = {} # Infinite Lightning
    a = []
    ability_desc = {}

class Hex(WeaponBase):
    ele = 'shadow'
    wt = 'sword'
    att = 743
    s3 = {} # Hexing Storm
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Absolute_Hex(WeaponBase):
    ele = 'shadow'
    wt = 'sword'
    att = 1485
    s3 = {} # Infinite Hexes
    a = []
    ability_desc = {}


flame = Absolute_Crimson
water = Absolute_Aqua
wind = Absolute_Tempest
light = Absolute_Lightning
shadow = Absolute_Hex