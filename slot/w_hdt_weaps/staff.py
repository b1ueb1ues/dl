from slot import *

class Brightblaze(WeaponBase):
    ele = 'flame'
    wt = 'staff'
    att = 684
    s3 = {} # Bright Flames
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Blazegambol(WeaponBase):
    ele = 'flame'
    wt = 'staff'
    att = 1368
    s3 = {} # Gambolling Flames
    a = []
    ability_desc = {}

class Unceasing_Tide(WeaponBase):
    ele = 'water'
    wt = 'staff'
    att = 670
    s3 = {} # Unceasing Stream
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Oceans_Embrace(WeaponBase):
    ele = 'water'
    wt = 'staff'
    att = 1340
    s3 = {} # Embracing Stream
    a = []
    ability_desc = {}

class Zephyrage(WeaponBase):
    ele = 'wind'
    wt = 'staff'
    att = 670
    s3 = {} # Bowing Gust
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Stormruler(WeaponBase):
    ele = 'wind'
    wt = 'staff'
    att = 1340
    s3 = {} # Guiding Gust
    a = []
    ability_desc = {}

class Shadowblot(WeaponBase):
    ele = 'light'
    wt = 'staff'
    att = 670
    s3 = {} # Illuminating Sneer
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Heavensneer(WeaponBase):
    ele = 'light'
    wt = 'staff'
    att = 1340
    s3 = {} # Trickster's Sneer
    a = []
    ability_desc = {}

class Creeping_Death(WeaponBase):
    ele = 'shadow'
    wt = 'staff'
    att = 670
    s3 = {} # Night Devourer
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Dark_Hunger(WeaponBase):
    ele = 'shadow'
    wt = 'staff'
    att = 1340
    s3 = {} # Despair Devourer
    a = []
    ability_desc = {}


flame = Blazegambol
water = Oceans_Embrace
wind = Stormruler
light = Heavensneer
shadow = Dark_Hunger