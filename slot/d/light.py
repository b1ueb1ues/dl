from slot import *

class Cupid(DragonBase):
    ele = 'light'
    att = 119

class C_Phoenix(DragonBase):
    ele = 'light'
    att = 124
    aura = ('att','passive',0.5)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('apl','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.paralysis.get()*0.2
