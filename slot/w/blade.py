from slot import *

class Conflagration(WeaponBase):
    ele = 'flame'
    wt = 'blade'
    att = 811
    s3 = {} # Conflagration Blade
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Blinding_Conflagration(WeaponBase):
    ele = 'flame'
    wt = 'blade'
    att = 1621
    s3 = {} # Blinding Blade
    a = []
    ability_desc = {}

class Torrent(WeaponBase):
    ele = 'water'
    wt = 'blade'
    att = 763
    s3 = {} # Torrent Blade
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Ruinous_Torrent(WeaponBase):
    ele = 'water'
    wt = 'blade'
    att = 1527
    s3 = {} # Surging Blade
    a = []
    ability_desc = {}

class Horizon(WeaponBase):
    ele = 'wind'
    wt = 'blade'
    att = 787
    s3 = {} # Horizon Blade
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Endless_Horizon(WeaponBase):
    ele = 'wind'
    wt = 'blade'
    att = 1574
    s3 = {} # Endless Blade
    a = []
    ability_desc = {}

class Flash(WeaponBase):
    ele = 'light'
    wt = 'blade'
    att = 748
    s3 = {} # Flashing Blade
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Brilliant_Flash(WeaponBase):
    ele = 'light'
    wt = 'blade'
    att = 1495
    s3 = {} # Brilliant Blade
    a = []
    ability_desc = {}

class Abyss(WeaponBase):
    ele = 'shadow'
    wt = 'blade'
    att = 811
    s3 = {} # Enigmatic Blade
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class True_Abyss(WeaponBase):
    ele = 'shadow'
    wt = 'blade'
    att = 1621
    s3 = {} # Hellish Blade
    a = []
    ability_desc = {}


flame = Blinding_Conflagration
water = Ruinous_Torrent
wind = Endless_Horizon
light = Brilliant_Flash
shadow = True_Abyss