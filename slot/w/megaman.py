from slot import *

class HDT1_Muspelheim(WeaponBase):
    ele = ['flame']
    wt = 'megaman'
    att = 727
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Crimson Flames
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Infernoblaze(WeaponBase):
    ele = ['flame']
    wt = 'megaman'
    att = 1453
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Adoring Flames
    a = []

class Chimeratech_Archmage(WeaponBase):
    ele = ['flame']
    wt = 'megaman'
    att = 1001
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Brisingr(WeaponBase):
    ele = ['flame']
    wt = 'megaman'
    att = 1590
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Brisingr(Agito_Brisingr):
    att = 1031
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

flame = HDT2_Infernoblaze
