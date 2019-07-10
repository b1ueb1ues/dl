from slot import *

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127

class Sakuya(DragonBase):
    ele = 'flame'
    att = 127
    aura = [('att','passive',0.2),
            ('s','passive',0.7)]


class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    aura = [('att','passive',0.45),
            ('crit','damage',0.55)]

