#unused now
import slot
from slot.a import *
import slot.w

def set(slots):
    ele = slots.c.ele
    wt = slots.c.wt
    stars = slots.c.stars
    name = slots.c.name


    if ele == 'flame':
        slots.d = slot.d.flame.Sakuya()
    elif ele == 'water':
        slots.d = slot.d.water.Siren()
    elif ele == 'wind':
        slots.d = slot.d.wind.Vayu()
    elif ele == 'light':
        if wt == 'dagger' or wt == 'bow' or wt == 'wand':
            slots.d = slot.d.light.Daikokuten()
        else:
            slots.d = slot.d.light.Cupid()
    elif ele == 'shadow':
        slots.d = slot.d.shadow.Shinobi()


    slots.a = RR()+CE()

    if wt == 'sword':
        slots.a = TSO()+BN()
    if wt == 'blade':
        slots.a = RR()+BN()
    if wt == 'dagger':
        if ele == 'water':
            slots.a = TB()+The_Prince_of_Dragonyule()
        elif ele == 'shadow':
            slots.a = TB()+HttH()
        else:
            slots.a = TB()+LC()
    if wt == 'axe':
        slots.a = KFM()+CE()
    if wt == 'lance': 
        slots.a = RR()+BN()
        #slots.a = LC()+Dragon_and_Tamer()
    if wt == 'wand': 
        slots.a = CC()+FoG()
    if wt == 'bow':
        slots.a = FB()+DD()
    

    slots.c.ex = {wt:('ex',wt)}
    #slots.c.ex = [('ex', 'blade'), ('ex', 'wand')]
    #if wt == 'dagger' :
    #    slots.c.ex = [('ex', 'blade'), ('ex', 'wand'), ('ex', 'dagger')]
    #elif wt == 'bow' :
    #    slots.c.ex = [('ex', 'blade'), ('ex', 'wand'), ('ex', 'bow')]

    typeweapon = getattr(slot.w, wt)
    weapon = getattr(typeweapon, ele)

    slots.w = weapon()

    return


