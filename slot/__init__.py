import copy


class Slot(object):
    att = 0
    ele = 'none'
    wt = 'none'
    stype = 'slot'
    onele = 0
    onwt = 0
    def __init__(this):
        this.mod = []
        this.conf = {}

    def setup(this, c):
        if c.ele == this.ele :
            this.onele = 1
        if c.wt == this.wt :
            this.onwt = 1


    def oninit(this, adv):
        adv.conf.update(this.conf)

        i = this.stype
        j = this.mod
        if type(j) == tuple:
            Modifier(i,*j)
        elif type(j) == list:
            idx = 0
            for k in j:
                Modifier(i+'_%d'%idx,*k)
                idx += 1


class CharacterBase(Slot):
    def setup(this):
        return 


class WeaponBase(Slot):
    stype = 'w'
    wt = 'none'
    s3 = {}

 #   def oninit(this, adv):
 #       super().oninit(adv)


    def setup(this, c):
        Slot.setup(this, c)
        if this.onele :
            this.att *= 1.5
            this.conf = this.s3
        elif this.ele == 'all' :
            this.conf = this.s3
        
        if not this.onwt :
            print('Weapon can\'t equip')
            errrrrrrrrrrrrr()



class DragonBase(Slot):
    stype = 'd'
    aura = ('att','passive',0.60)

    def setup(this, c):
        Slot.setup(this, c)
        if this.onele:
            this.att *= 1.5
            this.mod = this.aura

    def oninit(this, adv):
        pass


class Amuletempty(object):
    stype = 'a2'
    def oninit(this,adv):
        return
    def setup(this, c):
        return


class AmuletBase(Slot):
    ae = Amuletempty()
    stype = 'a1'
    a2 = None

    def __add__(this, another):
        this.a2 = another
        this.a2.stype = 'a2'
        return this


 #   def oninit(this, adv):
 #       if this.a2:
 #           this.a2.a2 = None
 #           this.a2.oninit(adv)
    
    

class Slots(object):
    #w = None 
    #d = None 
    #a = None 
    #a2 = None
    #w = WeaponBase()
    #d = DragonBase()
    #a = AmuletBase()+AmuletBase()
    #c = CharacterBase()
    #a2 = AmuletBase()
    def __init__(this):
        this.c = CharacterBase()
        this.w = WeaponBase()
        this.d = DragonBase()
        this.a = AmuletBase()+AmuletBase()
        return
        #import conf.csv2conf
        #this.name = name
        #this.conf = conf.csv2conf.get(name)
        #this.c.ele = this.conf['element']
        #this.c.wt = this.conf['weapon']
        #this.c.att = this.conf['str_adv']

    def __setup(this):
        this.c.setup()
        this.w.setup(this.c)
        this.d.setup(this.c)
        this.a.setup(this.c)


    def oninit(this, adv):
        tmp = copy.deepcopy(this)
        this.tmp = tmp
        tmp.__setup()
        tmp.c.oninit(adv)
        tmp.w.oninit(adv)
        tmp.d.oninit(adv)
        tmp.a.oninit(adv)

    def att(this, forte=None):
        tmp = copy.deepcopy(this)
        this.tmp = tmp
        tmp.__setup()
        if not forte:
            return tmp.c.att + tmp.d.att + tmp.w.att + tmp.a.att
        return tmp.c.att*forte.c(tmp.c.ele,tmp.c.wt) + tmp.d.att*forte.d(tmp.d.ele) + tmp.w.att + tmp.a.att

    def _att(this, forte=None):
        a = this.att(forte)
        dm = this.tmp.d.mod
        md = 0
        if type(dm)==list:
            for i in dm:
                if i[0] == 'att':
                    md = i[2]
        elif type(dm)==tuple:
            if dm[0] == 'att':
                md = dm[2]
        return a+a*md

import slot.d as d
import slot.w as w
import slot.a as a

def main():
    s = Slots('elisanne')
    import slot
    slot.DragonBase = DragonBase
    #slot.d.base(DragonBase)
    import slot.d.water
    import slot.d.flame
    s.d = slot.d.water.Dragon()
    s.setup()
    print(s.d.att)

if __name__ == "__main__":
    main()
