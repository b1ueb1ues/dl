import bow

conf = {}
conf.update(bow.conf)

conf.update({
        "s3_dmg"      : 3*3.16   ,
        "s3_sp"       : 7501     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.75     ,
    })

conf['str_w'] = 1.5 * 534
