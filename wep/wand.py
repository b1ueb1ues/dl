from core import Conf

conf = Conf()

conf = {}
conf.update( {
        "xtype"         : "ranged" ,

        "x1.dmg"         : 0.98     ,
        "x1.sp"          : 130      ,
        "x1.startup"     : 18/60.0  ,
        "x1.recovery"    : 33/60.0  ,

        "x2.dmg"         : 0.53*2   ,
        "x2.sp"          : 200      ,
        "x2.startup"     : 0        ,
        "x2.recovery"    : 31/60.0  ,

        "x3.dmg"         : 0.36*3   ,
        "x3.sp"          : 240      ,
        "x3.startup"     : 0        ,
        "x3.recovery"    : 53/60.0  ,

        "x4.dmg"         : 0.78*2   ,
        "x4.sp"          : 430      ,
        "x4.startup"     : 0        ,
        "x4.recovery"    : 64/60.0  ,

        "x5.dmg"         : 0.3605*4+0.618 ,
        "x5.sp"          : 600      ,
        "x5.startup"     : 0        ,
        #"x5.recovery"    : 68/60.0  ,
        "x5.recovery"    : 29/60.0  ,

        "fs._startup"    : 0        ,
        "fs._recovery"   : 29/60.0  ,

        "fs.dmg"         : 0.9*2    ,
        "fs.sp"          : 400      ,
        "fs.startup"     : 42/60.0  ,
        "fs.recovery"    : 81/60.0  ,

        "dodge_recovery" : 43/60.0  ,

        "missile_iv"  : {
            "fs" : 0.7/2 ,
            "x1" : 0.7   ,
            "x2" : 0.7   ,
            "x3" : 0.7   ,
            "x4" : 0.7   ,
            "x5" : 0.7   ,
            }, 
        })
