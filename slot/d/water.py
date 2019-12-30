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

class Simurgh(DragonBase):
    ele = 'water'
    att = 113
    aura = ('att','killer',0.6,'overdrive')

class Halloween_Maritimus(DragonBase):
    ele = 'water'
    att = 120
    aura = [('sp','passive',0.35)]

H_Maritimus = Halloween_Maritimus
