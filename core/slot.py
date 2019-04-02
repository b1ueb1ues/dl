import conf

class Slot(object):
    conf = {
        }
    def __init__(this):
        pass

    def onele(this, ele):
        pass

    def oninit(this, adv):
        pass

class CharacterBase(Slot):
    name = ''
    pass

class WeaponBase(Slot):
    def __init__(this, s3conf):
        this.s3conf = s3conf

    def oninit(this, adv):
        adv.conf.update(this.s3conf)

    def onele(this, ele):
        this.conf['str'] *= 1.5

class DragonBase(Slot):
    def onele(this, ele):
        this.conf['str'] *= 1.5
        this.conf['mod'] = ('att','passive',0.60)

    def oninit(this, adv):
        pass

class AmuletBase(Slot):
    conf = {
        'ele':'all',
        'stars':5,
        'str':64,
        "mod":[('s', 'passive', 0.25) ,
               ('crit', 'chance', 0.06, 'hp70')],
        }
    pass



class Slots(object):
    c = None #CharacterBase()
    w = None #WeaponBase()
    d = None #DragonBase()
    a = None #AmuletBase()
    def __init__(this,name):
        this.c = CharacterBase()
        this.c.name = name

    def setup(this):
        this.conf = {}
        this.conf['stars'] = c.stars
        this.conf['element'] = c.ele

if __name__ == "__main__":
    s = Slots('mikoto')
