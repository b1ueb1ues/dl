from slot import *

class HDT1_Conflagration(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 811
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    } # Conflagration Blade
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Blinding_Conflagration(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 1621
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    } # Blinding Blade
    a = []

class HDT1_Torrent(WeaponBase):
    ele = ['water']
    wt = 'blade'
    att = 763
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    } # Torrent Blade
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Ruinous_Torrent(WeaponBase):
    ele = ['water']
    wt = 'blade'
    att = 1527
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 7227     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    } # Surging Blade
    a = []

class HDT1_Horizon(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 787
    s3 = {
        "dmg"      : 9.57   ,
        "sp"       : 7582   ,
        "startup"  : 0.1    ,
        "recovery" : 2.35   ,
    } # Horizon Blade
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Endless_Horizon(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 1574
    s3 = {
        "dmg"      : 9.57   ,
        "sp"       : 7582   ,
        "startup"  : 0.1    ,
        "recovery" : 2.35   ,
    } # Endless Blade
    a = []

class HDT1_Flash(WeaponBase):
    ele = ['light']
    wt = 'blade'
    att = 748
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    } # Flashing Blade
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Brilliant_Flash(WeaponBase):
    ele = ['light']
    wt = 'blade'
    att = 1495
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    } # Brilliant Blade
    a = []

class HDT1_Abyss(WeaponBase):
    ele = ['shadow']
    wt = 'blade'
    att = 811
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    } # Enigmatic Blade
    a = [('k', 0.3, 'vs HJP')]

class HDT2_True_Abyss(WeaponBase):
    ele = ['shadow']
    wt = 'blade'
    att = 1621
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 6925   ,
        "startup"  : 0.1    ,
        "recovery" : 2.68   ,
    } # Hellish Blade
    a = []

class Chimeratech_Lord(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 1061
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Tyrfing(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 1636
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Tyrfing(Agito_Tyrfing):
    att = 1051
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

flame = HDT2_Blinding_Conflagration
water = HDT2_Ruinous_Torrent
wind = HDT2_Endless_Horizon
light = HDT2_Brilliant_Flash
shadow = HDT2_True_Abyss