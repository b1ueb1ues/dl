from slot import *

class Cupid(DragonBase):
    ele = 'light'
    att = 119

class LightSkillDmg(DragonBase):
    ele = 'light'
    att = 125
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]
