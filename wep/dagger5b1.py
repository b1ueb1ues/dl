import dagger

conf = {}
conf.update(dagger.conf)


conf.update({
        "s3_dmg"      : 6*1.64   ,
        "s3_sp"       : 7323     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.5      ,
    })
