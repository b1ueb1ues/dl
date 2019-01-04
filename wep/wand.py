
conf = {}
conf.update( {
        "x_type"         : "ranged" ,

        "x1_dmg"         : 0.98     ,
        "x1_sp"          : 130      ,
        "x1_startup"     : 18/60.0  ,
        "x1_recovery"    : 33/60.0  ,

        "x2_dmg"         : 1.06     ,
        "x2_sp"          : 200      ,
        "x2_startup"     : 0        ,
        "x2_recovery"    : 31/60.0  ,

        "x3_dmg"         : 1.08     ,
        "x3_sp"          : 240      ,
        "x3_startup"     : 0        ,
        "x3_recovery"    : 53/60.0  ,

        "x4_dmg"         : 1.56     ,
        "x4_sp"          : 430      ,
        "x4_startup"     : 0        ,
        "x4_recovery"    : 64/60.0  ,

        "x5_dmg"         : 2.06     ,
        "x5_sp"          : 600      ,
        "x5_startup"     : 0        ,
        "x5_recovery"    : 68/60.0  ,

        "fs_dmg"         : 1.8      ,
        "fs_sp"          : 400      ,
        "fs_startup"     : 42/60.0  ,
        "fs_recovery"    : 81/60.0  ,

        "dodge_recovery" : 43/60.0  ,

        "missile_iv"  : {
            "fs" : 0.7/2 ,
            "x1" : 0.7   ,
            "x2" : 0.7   ,
            "x3" : 0.7   ,
            "x4" : 0.7   ,
            "x5" : 0.7   ,
            }, 

        "mod_wep" : ('crit','chance',0.02),

        })

import wand5b1
import wand5b2

flame  = wand5b1
wind   = wand5b1
shadow = wand5b1

water  = wand5b2
light  = wand5b2

