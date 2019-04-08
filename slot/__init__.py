
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


class Amuletempty(object):
    def onele(this,ele):
        return
    def oninit(this,adv):
        return

class AmuletBase(Slot):
    ele = 'none'
    att = 0
    mod = []
    a2 = None
    def __init__(this):
        this.a2 = Amuletempty()

    def __add__(this, another):
        this.a2 = another
        return this
    
    

class Slots(object):
    #w = None 
    #d = None 
    #a = None 
    #a2 = None
    w = WeaponBase({})
    d = DragonBase()
    a = AmuletBase()+AmuletBase()
    #a2 = AmuletBase()
    def __init__(this,name):
        import conf.csv2conf
        this.name = name
        this.conf = conf.csv2conf.get(name)
        this.ele = this.conf['element']
        this.wt = this.conf['weapon']
        this.att = this.conf['str_adv']

    def setup(this):
        if this.ele == this.w.ele or this.w.ele=='all':
            this.w.onele(this.ele)
        if this.ele == this.d.ele or this.d.ele=='all':
            this.d.onele(this.ele)
        if this.ele == this.a.ele or this.a.ele=='all':
            this.a.onele(this.ele)
      #  if this.ele == this.a2.ele or this.a2.ele=='all':
      #      this.a2.onele(this.ele)

    def init(this, adv):
        this.w.oninit(adv)
        this.d.oninit(adv)
        this.a.oninit(adv)

    def att(this, forte=None):
        if not forte:
            return this.att + this.d.att + this.w.att + this.a.att + this.a.a2.att
        return this.att*forte.c(this.ele,this.wt) + this.d.att*forte.d(this.ele) + this.w.att + this.a.att + this.a.a2.att


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
