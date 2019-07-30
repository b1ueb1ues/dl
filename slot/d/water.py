from slot import *

class DJ(DragonBase):
    ele = 'water'
    att = 125
    aura = [('att','passive',0.45),
            ('crit','chance',0.2)]

class Siren(DragonBase):
    ele = 'water'
    att = 125
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]


class Leviathan(DragonBase):
    ele = 'water'
    att = 125

