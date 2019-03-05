import conf.slot_common

class Slot(object):
    conf = {
        'element','all',
        'stars',5,
        'str':64,
        "mod"  :[('s'    , 'passive' , 0.25) ,
                ('crit' , 'chance'  , 0.06)],
        }
    def onele(this):
        pass

    def init(this):
        pass

class Weapon(Slot):
    def onele(this):
        this.conf['str'] *= 1.5

class Dragon(Slot):
    def onele(this):
        this.conf['str'] *= 1.5

class Wp(Slot):
    pass



class Slots(object):
    a = {}
    d = {}
    wp = {}
    w = {}
