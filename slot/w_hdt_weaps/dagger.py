from slot import *

class Crimson_Fang(WeaponBase):
    ele = 'flame'
    wt = 'dagger'
    att = 728
    s3 = {} # Savage Crimson
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Flamerulers_Maw(WeaponBase):
    ele = 'flame'
    wt = 'dagger'
    att = 1455
    s3 = {} # Savage Flameruler
    a = []
    ability_desc = {}

class Tidal_Fang(WeaponBase):
    ele = 'water'
    wt = 'dagger'
    att = 728
    s3 = {} # Vicious Tides
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Tiderulers_Maw(WeaponBase):
    ele = 'water'
    wt = 'dagger'
    att = 1455
    s3 = {} # Vicious Tideruler
    a = []
    ability_desc = {}

class Galestorm_Fang(WeaponBase):
    ele = 'wind'
    wt = 'dagger'
    att = 691
    s3 = {} # Merciless Galestorm
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Windrulers_Maw(WeaponBase):
    ele = 'wind'
    wt = 'dagger'
    att = 1383
    s3 = {} # Merciless Windruler
    a = []
    ability_desc = {}

class Lightning_Fang(WeaponBase):
    ele = 'light'
    wt = 'dagger'
    att = 706
    s3 = {} # Ferocious Lightning
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Fulminators_Maw(WeaponBase):
    ele = 'light'
    wt = 'dagger'
    att = 1412
    s3 = {} # Ferocious Fulminator
    a = []
    ability_desc = {}

class Darkened_Fang(WeaponBase):
    ele = 'shadow'
    wt = 'dagger'
    att = 706
    s3 = {} # Bloodstarved Darkness
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Shaderulers_Maw(WeaponBase):
    ele = 'shadow'
    wt = 'dagger'
    att = 1412
    s3 = {} # Bloodstarved Shadowruler
    a = []
    ability_desc = {}


flame = Flamerulers_Maw
water = Tiderulers_Maw
wind = Windrulers_Maw
light = Fulminators_Maw
shadow = Shaderulers_Maw