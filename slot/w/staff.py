from slot import WeaponBase
from slot.w import agito_buffs

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

class Chimeratech_Staff(WeaponBase):
    ele = ['flame', 'shadow', 'wind']
    wt = 'staff'
    att = 877
    s3 = {} #
    a = [('uo', 0.04)]

class Agito2_Gjallarhorn(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1612
    s3 = agito_buffs['flame'][1]

class Agito1_Goosefoot_Staff(WeaponBase):
    ele = ['shadow']
    wt = 'staff'
    att = 1467
    s3 = agito_buffs['shadow'][1]

class Agito1_Gjallarhorn(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1467
    s3 = agito_buffs['flame'][1]

class Agito1_Avalon(WeaponBase):
    ele = ['wind']
    wt = 'staff'
    att = 1467
    s3 = agito_buffs['wind'][1]

class UnreleasedAgitoStr_WaterStaff(Agito1_Gjallarhorn):
    ele = ['water']

class UnreleasedAgitoStr_LightStaff(Agito1_Gjallarhorn):
    ele = ['light']

class UnreleasedAgitoSpd_WaterStaff(Agito1_Goosefoot_Staff):
    ele = ['water']

class UnreleasedAgitoSpd_LightStaff(Agito1_Goosefoot_Staff):
    ele = ['light']

flame = Agito2_Gjallarhorn
water = HDT2_Oceans_Embrace
wind = Agito1_Avalon
light = HDT2_Heavensneer
shadow = Agito1_Goosefoot_Staff
