from slot import *

class Dragonyule_Jeanne(DragonBase):
    ele = 'water'
    att = 125
    aura = [('att','passive',0.45),
            ('crit','chance',0.2)]
DJ = Dragonyule_Jeanne

class Siren(DragonBase):
    ele = 'water'
    att = 125
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Leviathan(DragonBase):
    ele = 'water'
    att = 125

class Vodyanoy(DragonBase):
    ele = 'water'
    att = 100
    aura = ('att','passive',0.45)

class Siren_0ub(DragonBase):
    ele = 'water'
    att = 57
    aura = [('att','passive',0.1),
            ('s','passive',0.7)]

class Simurgh(DragonBase):
    ele = 'water'
    att = 113
    aura = ('att','killer',0.6,'overdrive')