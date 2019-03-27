

def get(s, e, w):
    d = {
        'ele','all',
        'str':127,
        'mod':('att','passive',0.6),
        }

    wp = {
        'ele','all',
        'str':64,
        "mod"  :[('s'    , 'passive' , 0.25) ,
                ('crit' , 'chance'  , 0.06)],
        }
    wp2 = {
        'ele','all',
        'str':64,
        "mod"  :[('crit'    , 'damage' , 1.13) ,
                ('crit' , 'chance'  , 0.08)],
        }

    return d, wp, wp2

