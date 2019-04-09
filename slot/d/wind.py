from slot import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127

class Longlong(DragonBase):
    ele = 'wind'
    att = 127
    aura = [('att','passive',0.45),
            ('crit','damage',0.55)]
