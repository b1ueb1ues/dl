from slot import *

class Crimson_Heat(WeaponBase):
    ele = 'flame'
    wt = 'axe'
    att = 780
    s3 = {} # Crimson Passion
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Royal_Crimson_Heat(WeaponBase):
    ele = 'flame'
    wt = 'axe'
    att = 1559
    s3 = {} # Royal Crimson Passion
    a = []
    ability_desc = {}

class Mercys_Tide(WeaponBase):
    ele = 'water'
    wt = 'axe'
    att = 756
    s3 = {} # Mercy's Embrace
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Mercys_Azure_Tide(WeaponBase):
    ele = 'water'
    wt = 'axe'
    att = 1512
    s3 = {} # Mercy's Azure Embrace
    a = []
    ability_desc = {}

class Storms_Guide(WeaponBase):
    ele = 'wind'
    wt = 'axe'
    att = 756
    s3 = {} # Storm's Wisdom
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Glorystorms_Guide(WeaponBase):
    ele = 'wind'
    wt = 'axe'
    att = 1512
    s3 = {} # Glorystorm's Wisdom
    a = []
    ability_desc = {}

class Thundercrash(WeaponBase):
    ele = 'light'
    wt = 'axe'
    att = 803
    s3 = {} # Thunder's Delight
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Mighty_Thundercrash(WeaponBase):
    ele = 'light'
    wt = 'axe'
    att = 1606
    s3 = {} # Mighty Thunder's Delight
    a = []
    ability_desc = {}

class Darkbite_Axe(WeaponBase):
    ele = 'shadow'
    wt = 'axe'
    att = 803
    s3 = {} # Darkbite's Curse
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Shadowy_Darkbite_Axe(WeaponBase):
    ele = 'shadow'
    wt = 'axe'
    att = 1606
    s3 = {} # Shadowy Darkbite's Curse
    a = []
    ability_desc = {}


flame = Royal_Crimson_Heat
water = Mercys_Azure_Tide
wind = Glorystorms_Guide
light = Mighty_Thundercrash
shadow = Shadowy_Darkbite_Axe