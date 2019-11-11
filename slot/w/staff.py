import slot
from slot import *


class staff5b1(WeaponBase):
    ele = ['flame','water','wind']
    wt = 'staff'
    att = 528
    s3 = {
        }

class staff5b2(WeaponBase):
    ele = ['light','shadow']
    wt = 'staff'
    att = 513
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 15205    ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

<<<<<<< HEAD
class staffHJPBane(WeaponBaseHJP):
    wt = 'staff'
    att = 317

flame  = staff5b1
water  = staff5b1
wind   = staff5b1
=======
class staff5d1flame(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 684
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        }
>>>>>>> 01fc3bdb99a2329a6c009c19b0b265de12e7ca46

class staff5d1water(WeaponBase):
    ele = ['water']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        }

class staff5d1wind(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        }

class staff5d1light(WeaponBase):
    ele = ['light']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        }

class staff5d1shadow(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        }

<<<<<<< HEAD

class HDT_Brightblaze(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 684
    s3 = {} # Bright Flames
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Blazegambol(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1368
    s3 = {} # Gambolling Flames
    a = []
    ability_desc = {}

class HDT_Unceasing_Tide(WeaponBase):
    ele = ['water']
    wt = 'staff'
    att = 670
    s3 = {} # Unceasing Stream
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Oceans_Embrace(WeaponBase):
    ele = ['water']
    wt = 'staff'
    att = 1340
    s3 = {} # Embracing Stream
    a = []
    ability_desc = {}

class HDT_Zephyrage(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 670
    s3 = {} # Bowing Gust
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Stormruler(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 1340
    s3 = {} # Guiding Gust
    a = []
    ability_desc = {}

class HDT_Shadowblot(WeaponBase):
    ele = ['light']
    wt = 'staff'
    att = 670
    s3 = {} # Illuminating Sneer
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Heavensneer(WeaponBase):
    ele = ['light']
    wt = 'staff'
    att = 1340
    s3 = {} # Trickster's Sneer
    a = []
    ability_desc = {}

class HDT_Creeping_Death(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 670
    s3 = {} # Night Devourer
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Dark_Hunger(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 1340
    s3 = {} # Despair Devourer
    a = []
    ability_desc = {}

=======
flame  = staff5d1flame
water  = staff5d1water
wind   = staff5d1wind
light  = staff5d1light
shadow = staff5d1shadow
>>>>>>> 01fc3bdb99a2329a6c009c19b0b265de12e7ca46
