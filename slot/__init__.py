
class Slot(object):
    conf = {
        }
    def __init__(this):
        pass

    def onele(this, ele):
        pass

    def oninit(this, adv):
        pass

class WeaponBase(Slot):
    att=100
    ele = 'all'
    def __init__(this, s3conf):
        this.s3conf = s3conf

    def oninit(this, adv):
        adv.conf.update(this.s3conf)

    def onele(this, ele):
        this.att *= 1.5

class DragonBase(Slot):
    att = 0
    ele = 'none'
    aura = ('att','passive',0.60)
    def onele(this, ele):
        this.att *= 1.5
        this.mod = this.aura

    def oninit(this, adv):
        pass

class AmuletBase(Slot):
    ele = 'all'
    att = 100
    mod = []

class Slots(object):
    #w = None 
    #d = None 
    #a = None 
    #a2 = None
    w = WeaponBase({})
    d = DragonBase()
    a = AmuletBase()
    a2 = AmuletBase()
    def __init__(this,name):
        import conf.csv2conf
        this.name = name
        this.conf = conf.csv2conf.get(name)
        this.ele = this.conf['element']
        this.weapon = this.conf['weapon']
        this.att = this.conf['str_adv']

    def setup(this):
        if this.ele == this.w.ele or this.w.ele=='all':
            this.w.onele(this.ele)
        if this.ele == this.d.ele or this.d.ele=='all':
            this.d.onele(this.ele)
        if this.ele == this.a.ele or this.a.ele=='all':
            this.a.onele(this.ele)
        if this.ele == this.a2.ele or this.a2.ele=='all':
            this.a2.onele(this.ele)

import d
import w
import a

def main():
    s = Slots('elisanne')
    import slot
    slot.DragonBase = DragonBase
    #slot.d.base(DragonBase)
    import slot.d.water
    import slot.d.flame
    s.d = slot.d.water.Dragon()
    s.setup()
    print s.d.att

if __name__ == "__main__":
    main()
