import dagger

conf = {}
conf.update(dagger.conf)

conf.update({
        "s3_buff"     : [0.4, 5, 'att','buff','self'],
        "s3_sp"       : 7103       ,
        "s3_startup"  : 0.10+0.15  ,
        "s3_recovery" : 1.05-0.15  ,
    })
conf['str_w'] = 1.5 * 529
