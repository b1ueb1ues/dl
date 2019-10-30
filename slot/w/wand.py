import slot
from slot import *

class wand5b2p2(WeaponBase):
    ele = ['all']
    wt = 'wand'
    att = 470
    s3 = {
        "dmg"      : 4*2.44   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wand4b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'wand'
    att = 372
    s3 = {
        "dmg"      : 9.84     ,
        "sp"       : 8453     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wand5b1(WeaponBase):
    ele = ['flame','wind','shadow']
    wt = 'wand'
    att = 528
    s3 = {
        }

class wand5b2(WeaponBase):
    ele = ['water','light']
    wt = 'wand'
    att = 573
    s3 = {
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

class wandHMSBane(WeaponBaseHMS):
    wt = 'wand'
    att = 351

class wandHBHBane(WeaponBaseHBH):
    wt = 'wand'
    att = 343

class wandHMCBane(WeaponBaseHMC):
    wt = 'wand'
    att = 372

class wandHZDBane(WeaponBaseHZD):
    wt = 'wand'
    att = 351

class wandHJPBane(WeaponBaseHJP):
    wt = 'wand'
    att = 351


flame  = wand5b1
wind   = wand5b1
shadow = wand5b1

water  = wand5b2
light  = wand5b2


class HDT_Muspelheim(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Crimson Flames
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Infernoblaze(WeaponBase):
    ele = ['flame']
    wt = 'wand'
    att = 1453
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Adoring Flames
    a = []
    ability_desc = {}

class HDT_Hydroballista(WeaponBase):
    ele = ['water']
    wt = 'wand'
    att = 727
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Flowing Waves
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Aquatic_Spiral(WeaponBase):
    ele = ['water']
    wt = 'wand'
    att = 1453
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Cascading Waves
    a = []
    ability_desc = {}

class HDT_Tornado_Tail(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 788
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Primal Cyclone
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Grand_Tempest(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 1575
    s3 = {
        "dmg"      : 4*2.43   ,
        "sp"       : 7635     ,
        "startup"  : 0.8      ,
        "recovery" : 1.0      ,
        } # Raging Cyclone
    a = []
    ability_desc = {}

class HDT_Crossed_Lightning(WeaponBase):
    ele = ['light']
    wt = 'wand'
    att = 765
    s3 = {} # Mirthful Lightning
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Primeval_Thunder(WeaponBase):
    ele = ['light']
    wt = 'wand'
    att = 1530
    s3 = {} # Ecstatic Lightning
    a = []
    ability_desc = {}

class HDT_Venomous_Curse(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 742
    s3 = {} # Enveloping Darkness
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_Darkbinder(WeaponBase):
    ele = ['shadow']
    wt = 'wand'
    att = 1484
    s3 = {} # Binding Darkness
    a = []
    ability_desc = {}

