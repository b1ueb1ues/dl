from slot import WeaponBase
from slot.w import agito_buffs

class HDT1_Muspelheim(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.8      ,
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 4        ,
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
        "hit"      : 1        ,
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
        "hit"      : 1        ,
    } # Binding Darkness
    a = []

class Chimeratech_Wand(WeaponBase):
    ele = ['flame', 'shadow']
    wt = 'wand'
    att = 1001
    s3 = {} #
    a = [('uo', 0.04)]

class Agito1_Brisingr(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 1590
    s3 = agito_buffs['flame'][1]

class Agito2_Brisinga(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 1747
    s3 = agito_buffs['flame'][1]

class Agito1_Jiu_Ci(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 1590
    s3 = agito_buffs['shadow'][1]

class Agito1_Camelot(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 1590
    s3 = agito_buffs['wind'][1]

class UnreleasedAgitoStr_WaterWand(Agito1_Brisingr):
    ele = ['water']

class UnreleasedAgitoStr_LightWand(Agito1_Brisingr):
    ele = ['light']

class UnreleasedAgitoSpd_WaterWand(Agito1_Jiu_Ci):
    ele = ['water']

class UnreleasedAgitoSpd_LightWand(Agito1_Jiu_Ci):
    ele = ['light']

flame = Agito2_Brisinga
water = HDT2_Aquatic_Spiral
wind = Agito1_Camelot
light = HDT2_Primeval_Thunder
shadow = Agito1_Jiu_Ci