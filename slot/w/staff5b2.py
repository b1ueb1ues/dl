import staff

conf = {}
conf.update(staff.conf)

conf.update({
        "s3_dmg"      : 7.55     ,
        "s3_sp"       : 15205    ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 1.9      ,
    })

conf['str_w'] = 1.5 * 513
