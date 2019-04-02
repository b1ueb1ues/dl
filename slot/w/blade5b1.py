import blade

conf = {}
conf.update(blade.conf)

conf.update({
        "s3_dmg"      : 3.54*3   ,
        "s3_sp"       : 8030     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.65      ,
    })
conf['str_w'] = 572*1.5
