import slot
from slot import *


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
        "s3_dmg"      : 4*2.71   ,
        "s3_sp"       : 8757     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
        }

flame  = wand5b1
wind   = wand5b1
shadow = wand5b1

water  = wand5b2
light  = wand5b2

