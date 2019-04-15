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
        "dmg"      : 4*2.71   ,
        "sp"       : 8757     ,
        "startup"  : 0.1      ,
        "recovery" : 1.9      ,
        }

flame  = wand5b1
wind   = wand5b1
shadow = wand5b1

water  = wand5b2
light  = wand5b2

