from slot import *
from core.log import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127

class Longlong(DragonBase):
    ele = 'wind'
    att = 127
    aura = [('att','passive',0.45),
            ('crit','damage',0.55)]

class Pazuzu(DragonBase):
    ele = 'wind'
    att = 126
    aura = ('att','passive',0.5)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('pzz','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.poison.get()*0.2

class Vayu(DragonBase):
    ele = 'wind'
    att = 126
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Vayu_0ub(DragonBase):
    ele = 'wind'
    att = 57
    aura = [('att','passive',0.1),
            ('s','passive',0.7)]

class Roc(DragonBase):
    ele = 'wind'
    att = 101
    aura = ('att', 'passive', 0.45)

class Freyja(DragonBase):
    ele = 'wind'
    att = 120
    aura = [('sp','passive',0.35)]

#class Hastur(DragonBase):
#    ele = 'wind'
#    att = 127
#    aura = ('att','passive',0.55)
#    
#    def oninit(this, adv):
#        DragonBase.oninit(this, adv)
#        this.adv = adv
#        adv.hastur_iscding = 0
#
#        def hastur_cooldown(this, t):
#            this.hastur_iscding = 0
#            log('cd','a1','end')
#
#        def hastur_act(this):
#            if not this.hastur_iscding :
#                this.hastur_iscding = 1
#                Timer(this.hastur_cooldown).on(15)
#                log('cd','hastur','start')
#                this.Selfbuff('hastur',0.1,10).on()
#
#        charge_i = adv.charge
#        def charge(this, name, sp):
#            if this.s1.check():
#                return charge_i(name, sp)
#            charge_i(name, sp)
#            if this.s1.check():
#                this.hastur_act()
#            
#        setattr(type(this.adv), 'hastur_cooldown', hastur_cooldown)
#        setattr(type(this.adv), 'hastur_act', hastur_act)
#        setattr(type(this.adv), 'charge', charge)


        
