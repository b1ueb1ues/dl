
conf = {}
conf.update( {
        "x_type"         : "ranged" ,

        "x1_dmg"         : 0.69     ,
        "x1_sp"          : 232      ,
        "x1_startup"     : 18/60.0  ,
        "x1_recovery"    : 29/60.0  ,

        "x2_dmg"         : 0.8      ,
        "x2_sp"          : 232      ,
        "x2_startup"     : 0        ,
        "x2_recovery"    : 42/60.0  ,

        "x3_dmg"         : 0.45*2   ,
        "x3_sp"          : 348      ,
        "x3_startup"     : 0        ,
        "x3_recovery"    : 38/60.0  ,

        "x4_dmg"         : 1.50     ,
        "x4_sp"          : 464      ,
        "x4_startup"     : 0        ,
        "x4_recovery"    : 67/60.0  ,

        "x5_dmg"         : 1.96     ,
        "x5_sp"          : 696      ,
        "x5_startup"     : 0        ,
        #"x5_recovery"    : 68/60.0  ,
        "x5_recovery"    : 40/60.0  ,

        "fsf_startup"    : 0        ,
        "fsf_recovery"   : 40/60.0  ,

        "fs_dmg"         : 0.61*4   ,
        "fs_sp"          : 580      ,
        "fs_startup"     : 42/60.0  ,
        "fs_recovery"    : 240/60.0 ,

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

import staff5b1
import staff5b2

flame  = staff5b1
water  = staff5b1
wind   = staff5b1

light  = staff5b2
shadow = staff5b2

