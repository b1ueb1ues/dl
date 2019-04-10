import copy
from core import Conf
from ability import *


class Slot(object):
    att = 0
    ele = 'none'
    wt = 'none'
    stype = 'slot'
    onele = 0
    onwt = 0
    def __init__(this):
        this.mod = []
        this.conf = Conf()
        this.a = []

    def setup(this, c):
        if c.ele == this.ele :
            this.onele = 1
        if c.wt == this.wt :
            this.onwt = 1


    def oninit(this, adv):
        adv.conf += this.conf

        i = this.stype
        j = this.mod
        if type(j) == tuple:
            adv.Modifier(i,*j)
        elif type(j) == list:
            idx = 0
            for k in j:
                adv.Modifier(i+'_%d'%idx,*k)
                idx += 1
        elif type(j) == dict:
            idx = 0
            for k in j:
                adv.Modifier(i+k+'_%d'%idx,*j[k])
                idx += 1


class CharacterBase(Slot):
    name = 'null'
    stars = 5
    def setup(this):
        return 


class WeaponBase(Slot):
    stype = 'w'
    wt = 'none'
    s3 = Conf()
    ele = [] # or ''

    def setup(this, c):
        super(WeaponBase, this).setup(c)
        if type(this.ele) == list:
            for i in this.ele:
                if c.ele == i :
                    this.onele = 1
                    break

        if this.onele :
            this.att *= 1.5
            this.conf = this.s3
        elif this.ele == 'all' :
            this.conf = this.s3
        
        if not this.onwt :
            print('Weapon can\'t equip')
            errrrrrrrrrrrrr()
        if not this.onele:
            print('!!!!!!!!!!\nwarning: weapon not onele')
            print this.ele, c.ele
            print('!!!!!!!!!!!\n')

        if this.wt == 'axe':
            this.mod.append(('crit','chance',0.04))
        else :
            this.mod.append(('crit','chance',0.02))



class DragonBase(Slot):
    stype = 'd'
    aura = ('att','passive',0.60)

    def setup(this, c):
        Slot.setup(this, c)
        if this.onele:
            this.att *= 1.5
            this.mod = this.aura


class Amuletempty(object):
    stype = 'a2'
    def oninit(this,adv):
        return
    def setup(this, c):
        return


class AmuletBase(Slot):
    ae = Amuletempty()
    stype = 'a'
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
        a = tmp.c.a + tmp.w.a + tmp.d.a + tmp.a.a
        print a
        adv.abilities = a
        print adv.__dict__
#        for i in a:
#            Ability(*i).oninit(adv)


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
