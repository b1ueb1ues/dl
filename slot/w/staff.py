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
    } # Despair Devourer
    a = []

class Void_Chimeratech_Cardinal(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 877
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Gjallarhorn(WeaponBase):
    ele = ['flame']
    wt = 'staff'
    att = 1467
    s3 = {} # Megingjörð
    a = []

flame = HDT2_Blazegambol
water = HDT2_Oceans_Embrace
wind = HDT2_Stormruler
light = HDT2_Heavensneer
shadow = HDT2_Dark_Hunger