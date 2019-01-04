import wand

conf = {}
conf.update(wand.conf)

conf.update({
        "s3_dmg"      : 4*2.71   ,
        "s3_sp"       : 8757     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
    })
