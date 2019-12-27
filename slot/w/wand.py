from slot import *

class HDT1_Muspelheim(WeaponBase):
    ele = ['flame']
    wt = 'wand'
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
    wt = 'wand'
    att = 1453
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Adoring Flames
    a = []

class HDT1_Hydroballista(WeaponBase):
    ele = ['water']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Flowing Waves
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Aquatic_Spiral(WeaponBase):
    ele = ['water']
    wt = 'wand'
    att = 1453
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Cascading Waves
    a = []

class HDT1_Tornado_Tail(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 788
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Primal Cyclone
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Grand_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 1575
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
    } # Raging Cyclone
    a = []

class HDT1_Crossed_Lightning(WeaponBase):
    ele = ['light']
    wt = 'wand'
    att = 765
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 7881     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9     ,
    } # Mirthful Lightning
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Primeval_Thunder(WeaponBase):
    ele = ['light']
    wt = 'wand'
    att = 1530
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 7881     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9     ,
    } # Ecstatic Lightning
    a = []

class HDT1_Venomous_Curse(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 742
    s3 = {
        "dmg"      : 9.74     ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.75     ,
    } # Enveloping Darkness
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Darkbinder(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 1484
    s3 = {
        "dmg"      : 9.74     ,
        "sp"       : 7635     ,
        "startup"  : 0.1      ,
        "recovery" : 1.75     ,
    } # Binding Darkness
    a = []

class Chimeratech_Archmage(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 1001
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Brisingr(WeaponBase):
    ele = ['flame']
    wt = 'wand'
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
water = HDT2_Aquatic_Spiral
wind = HDT2_Grand_Tempest
light = HDT2_Primeval_Thunder
shadow = HDT2_Darkbinder