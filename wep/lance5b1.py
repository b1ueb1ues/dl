import lance

conf = {}
conf.update(lance.conf)

conf.update({
        "s3_dmg"      : 2*4.61   ,
        "s3_sp"       : 8111     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
    })
