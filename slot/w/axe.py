from slot import *
import slot

class HDT1_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 780
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Crimson Passion
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Royal_Crimson_Heat(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1559
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Royal Crimson Passion
    a = []

class HDT1_Mercys_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 756
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    } # Mercy's Embrace
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Mercys_Azure_Tide(WeaponBase):
    ele = ['water']
    wt = 'axe'
    att = 1512
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    } # Mercy's Azure Embrace
    a = []

class HDT1_Storms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 756
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Storm's Wisdom
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Glorystorms_Guide(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 1512
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Glorystorm's Wisdom
    a = []

class HDT1_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 803
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    } # Thunder's Delight
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Mighty_Thundercrash(WeaponBase):
    ele = ['light']
    wt = 'axe'
    att = 1606
    s3 = {
        "dmg"      : 2.26*5   ,
        "sp"       : 8260     ,
        "startup"  : 0.1      ,
        "recovery" : 4.08     ,
    } # Mighty Thunder's Delight
    a = []

class HDT1_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 803
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Darkbite's Curse
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Shadowy_Darkbite_Axe(WeaponBase):
    ele = ['shadow']
    wt = 'axe'
    att = 1606
    s3 = {
        "dmg"      : 4.18*3   ,
        "sp"       : 8895     ,
        "startup"  : 0.1      ,
        "recovery" : 2.12     ,
    } # Shadowy Darkbite's Curse
    a = []

class Void_Chimeratech_Warlord(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1051
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Mjolnir(WeaponBase):
    ele = ['flame']
    wt = 'axe'
    att = 1621
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Mjolnir(Agito_Mjolnir):
    att = 1051
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

flame  = HDT2_Royal_Crimson_Heat
water  = HDT2_Mercys_Azure_Tide
wind   = HDT2_Glorystorms_Guide
light  = HDT2_Mighty_Thundercrash
shadow = HDT2_Shadowy_Darkbite_Axe