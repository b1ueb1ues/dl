from slot import *

class HDT1_Brightblaze(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 684
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Bright Flames
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Blazegambol(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1368
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Gambolling Flames
    a = []

class HDT1_Unceasing_Tide(WeaponBase):
    ele = ['water']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Unceasing Stream
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Oceans_Embrace(WeaponBase):
    ele = ['water']
    wt = 'staff'
    att = 1340
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Embracing Stream
    a = []

class HDT1_Zephyrage(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Bowing Gust
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Stormruler(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 1340
    s3 = {
        "dmg"      : 1.43*4   ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.77     ,
        "hit"      : 4        ,
    } # Guiding Gust
    a = []

class HDT1_Shadowblot(WeaponBase):
    ele = ['light']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        "hit"      : 1        ,
    } # Illuminating Sneer
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Heavensneer(WeaponBase):
    ele = ['light']
    wt = 'staff'
    att = 1340
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        "hit"      : 1        ,
    } # Trickster's Sneer
    a = []

class HDT1_Creeping_Death(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 670
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        "hit"      : 1        ,
    } # Night Devourer
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Dark_Hunger(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 1340
    s3 = {
        "dmg"      : 7.55     ,
        "sp"       : 13684    ,
        "startup"  : 0.1      ,
        "recovery" : 1.57     ,
        "hit"      : 1        ,
    } # Despair Devourer
    a = []

class Chimeratech_Cardinal(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 877
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Gjallarhorn(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1467
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Gjallarhorn(Agito_Gjallarhorn):
    att = 951
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

class UnreleasedAgito_WaterStaff(Agito_Gjallarhorn):
    ele = ['water']

class UnreleasedAgito_WindStaff(Agito_Gjallarhorn):
    ele = ['wind']

class UnreleasedAgito_LightStaff(Agito_Gjallarhorn):
    ele = ['light']

class UnreleasedAgito_ShadowStaff(Agito_Gjallarhorn):
    ele = ['shadow']

flame = Agito_Gjallarhorn
water = HDT2_Oceans_Embrace
wind = HDT2_Stormruler
light = HDT2_Heavensneer
shadow = HDT2_Dark_Hunger