from core import Conf

conf = Conf()

conf = {}
conf.update( {
        "xtype"         : "ranged" ,

        "x1.dmg"         : 0.30     ,
        "x1.sp"          : 80       ,
        "x1.startup"     : 18/60.0  ,
        "x1.recovery"    : 33/60.0  ,

        "x2.dmg"         : 0.30     ,
        "x2.sp"          : 80       ,
        "x2.startup"     : 18/60.0  ,
        "x2.recovery"    : 33/60.0  ,
        
        "x3.dmg"         : 0.30     ,
        "x3.sp"          : 80       ,
        "x3.startup"     : 18/60.0  ,
        "x3.recovery"    : 33/60.0  ,

        "x4.dmg"         : 0.30     ,
        "x4.sp"          : 80       ,
        "x4.startup"     : 18/60.0  ,
        "x4.recovery"    : 33/60.0  ,

        "x5.dmg"         : 0.30     ,
        "x5.sp"          : 80       ,
        "x5.startup"     : 18/60.0  ,
        "x5.recovery"    : 33/60.0  ,

        "fs._startup"    : 0        ,
        "fs._recovery"   : 29/60.0  ,

        "fs.dmg"         : 0.90     ,
        "fs.sp"          : 400      ,
        "fs.startup"     : 42/60.0  ,
        "fs.recovery"    : 81/60.0  ,

        "dodge.recovery" : 43/60.0  ,

        "missile_iv"  : {
            #"fs" : 0.7/2 ,
            #"x1" : 0.7   ,
            #"x2" : 0.7   ,
            #"x3" : 0.7   ,
            #"x4" : 0.7   ,
            #"x5" : 0.7   ,
            "fs" : 0   ,
            "x1" : 0   ,
            "x2" : 0   ,
            "x3" : 0   ,
            "x4" : 0   ,
            "x5" : 0   ,
            }, 
        })
