import blade

conf = {}
conf.update(blade.conf)
conf.update({
        "s3_dmg"      : 2.13*5   ,
        "s3_sp"       : 7695     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 2.65     ,
    })
conf['str_w'] = 590*1.5
