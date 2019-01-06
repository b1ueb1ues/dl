import axe 

conf = {}
conf.update(axe.conf)

conf.update({
        "s3_buff"     : [0.5, 20, 'crit','dmg'],
        "s3_sp"       : 4711       ,
        "s3_startup"  : 0.10+0.15  ,
        "s3_recovery" : 1.05-0.15  ,
    })

conf['str_w'] = 1.5 * 567
